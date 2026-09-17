import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from backend.config import settings
from backend.agent.agent import CustomerResolutionAgent
from backend.agent.schemas import ChatRequest, AgentResponse
from backend.tools.customer_tools import load_customers, get_customer_by_id
from backend.tools.booking_tools import load_bookings, get_bookings_for_customer, get_booking_by_id
from backend.tools.action_tools import execute_refund, issue_gesture_voucher
from backend.tools.escalation_tools import get_open_escalations

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API for AI-Based Customer Resolution System"
)

# Enable CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = CustomerResolutionAgent()

@app.get("/")
def root():
    return {"message": "AI-Based Customer Resolution API is running", "version": settings.VERSION}

@app.get("/api/customers")
def get_all_customers():
    return load_customers()

@app.get("/api/customers/{customer_id}")
def get_customer_details(customer_id: str):
    cust = get_customer_by_id(customer_id)
    if not cust:
        raise HTTPException(status_code=404, detail="Customer not found")
    return cust

@app.get("/api/bookings")
def get_bookings(customer_id: Optional[str] = Query(None)):
    if customer_id:
        return get_bookings_for_customer(customer_id)
    return load_bookings()

@app.post("/api/chat", response_model=AgentResponse)
def handle_chat(request: ChatRequest):
    return agent.process_request(request)

@app.post("/api/actions/refund")
def process_refund(booking_id: str, amount: float, reason: str = "Customer resolution"):
    return execute_refund(booking_id, amount, reason)

@app.post("/api/actions/voucher")
def process_voucher(customer_id: str, amount: float):
    return issue_gesture_voucher(customer_id, amount)

@app.get("/api/escalations")
def list_escalations():
    return get_open_escalations()

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host=settings.HOST, port=settings.PORT, reload=True)
