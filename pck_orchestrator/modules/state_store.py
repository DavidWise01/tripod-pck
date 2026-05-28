from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict


def load_state(path: Path) -> Dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"schema": "PCK.STATE.v0.1", "continuity_root": None, "events_seen": 0, "counts": {}}


def append_jsonl(path: Path, obj: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, sort_keys=True) + "\n")


def handle(event: Dict[str, Any], record: Dict[str, Any], ctx: Dict[str, Any]) -> Dict[str, Any]:
    state_path = ctx["base"] / ctx["config"]["paths"]["state"]
    ledger_path = ctx["base"] / ctx["config"]["paths"]["ledger"]
    state = load_state(state_path)
    state["continuity_root"] = record["continuity_root"]
    state["events_seen"] = int(state.get("events_seen", 0)) + 1
    counts = state.setdefault("counts", {})
    counts[record["primitive_state"]] = counts.get(record["primitive_state"], 0) + 1
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    append_jsonl(ledger_path, {"event": event, "record": record})
    return {"module": "state_store", "status": "ok", "continuity_root": state["continuity_root"]}
