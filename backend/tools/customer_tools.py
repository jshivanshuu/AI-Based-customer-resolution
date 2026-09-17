import json
from pathlib import Path

from langchain_core.tools import tool


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "customers.json"


def load_customers():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@tool
def get_customer(pnr: str):
    """
    Retrieve customer information using their PNR.
    """

    customers = load_customers()

    for customer in customers:
        if customer["pnr"] == pnr:
            return customer

    return {
        "error": "Customer not found",
        "pnr": pnr
    }