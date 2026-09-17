import json
from typing import Optional, Dict, Any, List
from backend.config import settings

def load_bookings() -> List[Dict[str, Any]]:
    if not settings.BOOKINGS_FILE.exists():
        return []
    with open(settings.BOOKINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_booking_by_id(booking_id: str) -> Optional[Dict[str, Any]]:
    bookings = load_bookings()
    for b in bookings:
        if b.get("id") == booking_id or b.get("flight") == booking_id or b.get("pnr") == booking_id:
            return b
    return None

def get_bookings_for_customer(customer_id: str) -> List[Dict[str, Any]]:
    bookings = load_bookings()
    return [b for b in bookings if b.get("pnr") == customer_id or b.get("customer_id") == customer_id]

