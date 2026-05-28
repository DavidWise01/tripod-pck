from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List
from schema import now_utc, stable_hash

ROOT_STATES = {"preserve", "prune", "assimilate"}
PRUNE_ACTIONS = {"block_publish", "quarantine", "reject_publish", "hold_private", "decay", "rest", "block_release"}
PRESERVE_ACTIONS = {"preserve", "preserve_reference", "publish", "publish_proof", "confirm_root", "increase_fitness"}
ASSIMILATE_ACTIONS = {"assimilate", "prune_raw_keep_wisdom", "choose_minimum_burden", "promote_wisdom", "fork", "route_branch", "assimilate_branch", "repair", "release", "mediate"}


def gate_eval(gate: str, values: List[bool]) -> bool:
    gate = gate.upper()
    if gate == "AND": return all(values)
    if gate == "OR": return any(values)
    if gate == "NOT": return not values[0] if values else True
    if gate == "XOR": return sum(bool(v) for v in values) == 1
    if gate == "NAND": return not all(values)
    if gate == "NOR": return not any(values)
    if gate == "XNOR": return all(values) or not any(values)
    raise ValueError(f"Unknown gate: {gate}")


def load_kernel(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collapse_actions(actions: set[str]) -> str:
    if actions & PRUNE_ACTIONS:
        return "prune"
    if actions & PRESERVE_ACTIONS:
        return "preserve"
    return "assimilate"


def evaluate(event: Dict[str, Any], kernel: Dict[str, Any], previous_root: str | None) -> Dict[str, Any]:
    signals = event.get("signals", {})
    triggered = []
    for rule in kernel.get("kernel_rules_27", []):
        inputs = rule.get("inputs", [])
        values = [bool(signals.get(name, False)) for name in inputs]
        if gate_eval(rule["gate"], values):
            triggered.append({
                "rule_id": rule["id"],
                "domain": rule["domain"],
                "action": rule["action"],
                "reason": rule["reason"],
            })
    actions = {t["action"] for t in triggered}
    primitive_state = collapse_actions(actions)
    record = {
        "schema": "PCK.EVAL.v0.1",
        "timestamp": now_utc(),
        "previous_root": previous_root,
        "event_id": event["event_id"],
        "event_hash": stable_hash(event),
        "triggered": triggered,
        "actions": sorted(actions),
        "primitive_state": primitive_state,
        "root_transition": f"{previous_root or 'GENESIS'} -> {primitive_state}",
    }
    record["record_hash"] = stable_hash(record)
    record["continuity_root"] = stable_hash({"previous_root": previous_root, "record_hash": record["record_hash"]})
    return record
