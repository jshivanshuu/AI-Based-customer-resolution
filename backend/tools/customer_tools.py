import json
from typing import Optional, Dict, Any, List
from backend.config import settings

def load_customers() -> List[Dict[str, Any]]:
    if not settings.CUSTOMERS_FILE.exists():
        return []
    with open(settings.CUSTOMERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_customer_by_id(customer_id: str) -> Optional[Dict[str, Any]]:
    customers = load_customers()
    for cust in customers:
        if cust.get("id") == customer_id or cust.get("pnr") == customer_id:
            return cust
    return None

def get_customer_by_pnr(pnr: str) -> Optional[Dict[str, Any]]:
    customers = load_customers()
    for cust in customers:
        if cust.get("pnr") == pnr:
            return cust
    return None

