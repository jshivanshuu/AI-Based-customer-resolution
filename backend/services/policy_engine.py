from typing import Dict, Any, Optional

class PolicyEngine:
    """
    Deterministic rules engine evaluating refund eligibility, cancellation fees,
    and automatic compensation vouchers based on service disruption parameters.
    """

    @staticmethod
    def evaluate_cancellation_policy(booking: Dict[str, Any], customer_tier: str) -> Dict[str, Any]:
        amount = float(booking.get("amount", 0.0))
        status = booking.get("status", "")
        delay_hours = float(booking.get("delay_hours", 0.0))
        is_refundable = booking.get("refundable", True)

        # Base calculations
        cancellation_fee = float(booking.get("cancellation_fee", 0.0))
        refund_amount = 0.0
        voucher_amount = 0.0
        escalation_required = False
        reasons = []

        # Tier benefits
        if customer_tier.lower() in ["platinum", "gold"]:
            cancellation_fee = 0.0
            reasons.append(f"Waived cancellation fee for {customer_tier} tier member.")

        # Flight delay compensation rules
        if status == "Cancelled" or delay_hours >= 4.0:
            refund_amount = amount
            cancellation_fee = 0.0
            if delay_hours >= 4.0:
                voucher_amount = 150.0 if customer_tier.lower() == "platinum" else 100.0
                reasons.append(f"Flight delayed by {delay_hours} hours. Full refund eligible + ${voucher_amount} compensation voucher.")
            elif status == "Cancelled":
                voucher_amount = 200.0
                reasons.append("Airline cancelled flight. Full refund eligible + $200 delay compensation voucher.")
        elif is_refundable:
            refund_amount = max(0.0, amount - cancellation_fee)
            reasons.append(f"Standard refund calculation: ${amount} minus ${cancellation_fee} fee.")
        else:
            refund_amount = 0.0
            reasons.append("Non-refundable booking according to standard terms.")

        # Escalation guardrail for large amounts
        if amount > 3000.0:
            escalation_required = True
            reasons.append("Booking amount exceeds automatic resolution threshold ($3,000). Escalation to human supervisor mandatory.")

        return {
            "eligible_for_refund": refund_amount > 0,
            "refund_amount": refund_amount,
            "cancellation_fee": cancellation_fee,
            "voucher_amount": voucher_amount,
            "escalation_required": escalation_required,
            "policy_summary": " | ".join(reasons)
        }
