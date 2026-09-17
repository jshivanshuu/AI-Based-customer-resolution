from typing import Dict, Any
from backend.services.policy_engine import PolicyEngine

def check_cancellation_policy(booking: Dict[str, Any], customer_tier: str = "Standard") -> Dict[str, Any]:
    """
    Wrapper tool to run policy checks for a given booking and customer tier.
    """
    return PolicyEngine.evaluate_cancellation_policy(booking, customer_tier)
