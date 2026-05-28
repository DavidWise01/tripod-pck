from __future__ import annotations
import json
from typing import Any, Dict


def handle(event: Dict[str, Any], record: Dict[str, Any], ctx: Dict[str, Any]) -> Dict[str, Any]:
    outbox = ctx["base"] / ctx["config"]["paths"]["outbox"]
    outbox.mkdir(parents=True, exist_ok=True)
    proof = {
        "schema": "PCK.PUBLIC.PROOF.v0.1",
        "event_id": event["event_id"],
        "event_hash": record["event_hash"],
        "record_hash": record["record_hash"],
        "continuity_root": record["continuity_root"],
        "timestamp": record["timestamp"],
    }
    proof_path = outbox / f"proof_{event['event_id'][:16]}.json"
    proof_path.write_text(json.dumps(proof, indent=2, sort_keys=True), encoding="utf-8")
    return {"module": "witness", "status": "proof_written", "path": str(proof_path)}
