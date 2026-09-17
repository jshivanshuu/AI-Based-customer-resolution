import uuid
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

ESCALATION_QUEUE: List[Dict[str, Any]] = []

def trigger_escalation(customer_id: str, reason: str, metadata: Optional[str] = None) -> Dict[str, Any]:
    """
    Creates an urgent supervisor escalation ticket.
    """
    escalation_id = f"ESC-{uuid.uuid4().hex[:6].upper()}"
    ticket = {
        "escalation_id": escalation_id,
        "customer_id": customer_id,
        "reason": reason,
        "metadata": metadata or "Triggered by resolution engine rule",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "OPEN",
        "priority": "HIGH"
    }
    ESCALATION_QUEUE.append(ticket)
    return ticket

def get_open_escalations() -> List[Dict[str, Any]]:
    return [e for e in ESCALATION_QUEUE if e["status"] == "OPEN"]
