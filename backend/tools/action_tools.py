from langchain_core.tools import tool


@tool
def execute_action(
    action: str,
    pnr: str
):
    """
    Execute an authorized airline customer-service action.
    """

    if action == "refund":
        return {
            "success": True,
            "action": "refund",
            "message": "Refund request initiated."
        }

    if action == "rebook":
        return {
            "success": True,
            "action": "rebook",
            "message": "Rebooking request initiated."
        }

    if action == "meal_voucher":
        return {
            "success": True,
            "action": "meal_voucher",
            "message": "₹500 meal voucher issued."
        }

    if action == "lounge_access":
        return {
            "success": True,
            "action": "lounge_access",
            "message": "Lounge access arranged."
        }

    if action == "hotel":
        return {
            "success": True,
            "action": "hotel",
            "message": "Hotel accommodation arranged for the eligible delayed-hours period."
        }

    return {
        "success": False,
        "message": "Unknown or unauthorized action."
    }