#!/usr/bin/env python3
from __future__ import annotations
import argparse
import importlib
import json
import time
from pathlib import Path
from typing import Any, Dict, List

from schema import normalize_event
from kernel import load_kernel, evaluate
from modules.state_store import load_state


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def clear_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")


def route_modules(record: Dict[str, Any], config: Dict[str, Any]) -> List[str]:
    routes = config.get("routes", {})
    modules = set(routes.get(record["primitive_state"], []))
    for action in record.get("actions", []):
        modules.update(routes.get(action, []))
    if not modules:
        modules.add("state_store")
    return sorted(modules)


def dispatch(module_name: str, event: Dict[str, Any], record: Dict[str, Any], ctx: Dict[str, Any]) -> Dict[str, Any]:
    mod = importlib.import_module(f"modules.{module_name}")
    return mod.handle(event, record, ctx)


def process_once(base: Path) -> List[Dict[str, Any]]:
    config = json.loads((base / "config.json").read_text(encoding="utf-8"))
    kernel = load_kernel(base / "kernel_rules.json")
    inbox = base / config["paths"]["inbox"]
    state_path = base / config["paths"]["state"]
    state = load_state(state_path)
    previous_root = state.get("continuity_root")
    raw_events = read_jsonl(inbox)[: int(config["valves"].get("max_events_per_run", 100))]
    results = []
    ctx = {"base": base, "config": config}
    for raw in raw_events:
        event = normalize_event(raw)
        event.setdefault("root_id", config.get("root_id", "0root.local"))
        record = evaluate(event, kernel, previous_root)
        modules = route_modules(record, config)
        module_results = []
        for name in modules:
            module_results.append(dispatch(name, event, record, ctx))
        previous_root = record["continuity_root"]
        results.append({"event_id": event["event_id"], "record": record, "modules": module_results})
    clear_file(inbox)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="PCK daemon: continuity event orchestrator")
    parser.add_argument("--base", default=Path(__file__).resolve().parent, type=Path)
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--sleep", default=5, type=int)
    args = parser.parse_args()
    if args.once:
        print(json.dumps(process_once(args.base), indent=2, sort_keys=True))
        return
    while True:
        results = process_once(args.base)
        if results:
            print(json.dumps(results, indent=2, sort_keys=True))
        time.sleep(args.sleep)


if __name__ == "__main__":
    main()
