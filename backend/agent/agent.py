import json
from typing import Dict, Any, List
from backend.agent.schemas import ChatRequest, AgentResponse, ActionProposal
from backend.agent.prompts import SYSTEM_RESOLUTION_PROMPT
from backend.services.policy_engine import PolicyEngine
from backend.tools.customer_tools import get_customer_by_id, get_customer_by_pnr
from backend.tools.booking_tools import get_booking_by_id
from backend.tools.escalation_tools import trigger_escalation

class CustomerResolutionAgent:
    """
    Autonomous agent orchestrating resolution logic, policy evaluations,
    tool execution, and automated action proposals.
    """

    def process_request(self, request: ChatRequest) -> AgentResponse:
        thoughts = []
        thoughts.append(f"Received resolution request for customer {request.customer_id}")

        customer = get_customer_by_pnr(request.customer_id) or get_customer_by_id(request.customer_id)
        if not customer:
            return AgentResponse(
                response_text="I'm sorry, I couldn't locate your customer profile in our system.",
                escalated=False,
                thought_process=thoughts
            )

        tier = customer.get("loyalty_tier") or customer.get("tier", "Standard")
        pnr = customer.get("pnr") or customer.get("id", "N/A")
        thoughts.append(f"Retrieved profile for {customer.get('name')} (PNR: {pnr}, Tier: {tier})")

        booking = get_booking_by_id(request.booking_id) if request.booking_id else None
        if booking:
            thoughts.append(f"Located active booking {booking.get('id')} ({booking.get('title')}) - Status: {booking.get('status')}")
        
        # Policy Evaluation
        policy_result = None
        if booking:
            policy_result = PolicyEngine.evaluate_cancellation_policy(booking, tier)
            thoughts.append(f"Policy engine decision: {policy_result['policy_summary']}")

        # Escalation Check
        user_msg = request.message.lower()
        if "legal" in user_msg or "lawyer" in user_msg or (policy_result and policy_result.get("escalation_required")):
            escalation_info = trigger_escalation(request.customer_id, request.message, "Policy threshold or sensitive keyword triggered")
            thoughts.append("Escalating ticket to Senior Supervisor queue")
            return AgentResponse(
                response_text=f"I understand your frustration. Due to the high priority of this case, I have escalated your request to a Senior Customer Supervisor. Reference ID: {escalation_info['escalation_id']}.",
                escalated=True,
                thought_process=thoughts
            )

        # Resolution Proposal Formulation
        proposal = None
        if policy_result and policy_result.get("eligible_for_refund"):
            refund_amt = policy_result.get("refund_amount", 0.0)
            voucher_amt = policy_result.get("voucher_amount", 0.0)
            proposal = ActionProposal(
                action_type="refund",
                amount=refund_amt + voucher_amt,
                details=f"Issue full refund of ${refund_amt:.2f} plus ${voucher_amt:.2f} delay compensation voucher.",
                requires_approval=False
            )
            response_text = (
                f"Hello {customer['name']}. I apologize for the disruption with your booking ({booking['title']}). "
                f"As a valued {tier} customer, you are eligible for a full refund of ${refund_amt:.2f}. "
                f"Additionally, we have issued a ${voucher_amt:.2f} travel voucher for your next journey."
            )
        elif booking:
            response_text = (
                f"Hello {customer['name']}. I have reviewed booking {booking['id']}. "
                f"According to policy: {policy_result['policy_summary']}. How else can I assist you today?"
            )
        else:
            response_text = f"Hello {customer['name']}! How can I assist you with your travel resolution today?"

        return AgentResponse(
            response_text=response_text,
            action_proposal=proposal,
            escalated=False,
            thought_process=thoughts
        )
