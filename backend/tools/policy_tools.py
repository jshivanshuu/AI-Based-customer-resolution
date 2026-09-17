from langchain_core.tools import tool

from services.policy_engine import resolve_policy
from tools.customer_tools import load_customers
from tools.booking_tools import load_bookings


@tool
def check_policy(
    intent: str,
    pnr: str,
    fare_difference: float = 0
):
    """
    Check whether a requested customer action is allowed
    under the supplied airline policy.
    """

    customers = load_customers()
    bookings = load_bookings()

    customer = None

    for c in customers:
        if c["pnr"] == pnr:
            customer = c
            break

    if customer is None:
        return {
            "allowed": False,
            "error": "Customer not found"
        }

    customer_bookings = [
        b for b in bookings
        if b["pnr"] == pnr
    ]

    if not customer_bookings:
        return {
            "allowed": False,
            "error": "Booking not found"
        }

    return resolve_policy(
        intent=intent,
        customer=customer,
        bookings=customer_bookings,
        fare_difference=fare_difference
    )