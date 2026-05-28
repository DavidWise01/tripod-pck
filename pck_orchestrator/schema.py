from __future__ import annotations
import datetime as dt
import json
import hashlib
from typing import Any, Dict


def now_utc() -> str:
    return dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"


def stable_hash(obj: Any) -> str:
    data = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def normalize_event(raw: Dict[str, Any]) -> Dict[str, Any]:
    event = dict(raw)
    event.setdefault("schema", "PCK.EVENT.v0.1")
    event.setdefault("timestamp", now_utc())
    event.setdefault("source", "unknown")
    event.setdefault("intent", "assimilate")
    event.setdefault("visibility", "private")
    event.setdefault("payload", {})
    event.setdefault("signals", {})
    # Mandatory continuity signals when present.
    event["signals"].setdefault("has_timestamp", bool(event.get("timestamp")))
    event["signals"].setdefault("has_actor", bool(event.get("actor") or event.get("source")))
    event["signals"].setdefault("has_session", bool(event.get("session") or event.get("root_id")))
    event["event_id"] = event.get("event_id") or stable_hash(event)
    return event
