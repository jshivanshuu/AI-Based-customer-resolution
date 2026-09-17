from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ChatMessage(BaseModel):
    sender: str = Field(..., description="Role: 'user', 'agent', or 'system'")
    text: str = Field(..., description="Content of the message")
    timestamp: Optional[str] = None

class ChatRequest(BaseModel):
    customer_id: str
    booking_id: Optional[str] = None
    message: str
    history: Optional[List[ChatMessage]] = []

class ActionProposal(BaseModel):
    action_type: str = Field(..., description="Type of action: refund, voucher, rebook, escalate")
    amount: Optional[float] = 0.0
    details: str
    requires_approval: bool = False

class AgentResponse(BaseModel):
    response_text: str
    action_proposal: Optional[ActionProposal] = None
    escalated: bool = False
    thought_process: List[str] = []
