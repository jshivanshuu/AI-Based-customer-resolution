import json
from pathlib import Path

from langchain_core.tools import tool


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "bookings.json"


def load_bookings():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@tool
def get_booking(pnr: str):
    """
    Retrieve booking and flight information for a customer's PNR.
    """

    bookings = load_bookings()

    results = [
        booking
        for booking in bookings
        if booking["pnr"] == pnr
    ]

    if not results:
        return {
            "error": "Booking not found",
            "pnr": pnr
        }

    return results