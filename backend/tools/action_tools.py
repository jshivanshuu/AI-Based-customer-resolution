import uuid
from typing import Dict, Any

def execute_refund(booking_id: str, amount: float, reason: str) -> Dict[str, Any]:
    """
    Executes refund processing to customer payment method.
    """
    transaction_id = f"TX-REF-{uuid.uuid4().hex[:8].upper()}"
    return {
        "status": "SUCCESS",
        "transaction_id": transaction_id,
        "booking_id": booking_id,
        "refund_amount": amount,
        "message": f"Refund of ${amount:.2f} successfully processed under transaction {transaction_id}."
    }

def issue_gesture_voucher(customer_id: str, amount: float, validity_days: int = 365) -> Dict[str, Any]:
    """
    Issues compensation/loyalty voucher code.
    """
    voucher_code = f"VOUCH-{uuid.uuid4().hex[:6].upper()}"
    return {
        "status": "ISSUED",
        "voucher_code": voucher_code,
        "customer_id": customer_id,
        "amount": amount,
        "validity_days": validity_days,
        "message": f"Issued gesture voucher {voucher_code} worth ${amount:.2f} valid for {validity_days} days."
    }
