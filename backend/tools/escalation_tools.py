from langchain_core.tools import tool


@tool
def escalate_to_human(
    pnr: str,
    reason: str
):
    """
    Escalate a customer request to human support.
    """

    return {
        "escalated": True,
        "pnr": pnr,
        "reason": reason,
        "status": "human_review_required"
    }