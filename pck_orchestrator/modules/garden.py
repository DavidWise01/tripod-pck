from __future__ import annotations
from typing import Any, Dict


def handle(event: Dict[str, Any], record: Dict[str, Any], ctx: Dict[str, Any]) -> Dict[str, Any]:
    # Placeholder for GitHub garden / peer discovery adapter.
    return {"module": "garden", "status": "noop_garden"}
