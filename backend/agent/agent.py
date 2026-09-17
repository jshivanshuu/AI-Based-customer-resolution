import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from .prompts import SYSTEM_PROMPT

from tools.customer_tools import get_customer
from tools.booking_tools import get_booking
from tools.policy_tools import check_policy
from tools.action_tools import execute_action
from tools.escalation_tools import escalate_to_human


load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is not set. Please add it to your .env file."
    )


tools = [
    get_customer,
    get_booking,
    check_policy,
    execute_action,
    escalate_to_human
]


MODELS_TO_TRY = [
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash"
]


def get_agent(model_name: str):
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0
    )
    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT
    )


def run_agent(message: str, pnr: str | None = None):
    if pnr:
        user_message = f"""
Customer PNR: {pnr}

Customer request:
{message}
"""
    else:
        user_message = message

    last_error = None

    for model_name in MODELS_TO_TRY:
        try:
            agent = get_agent(model_name)
            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_message
                        }
                    ]
                }
            )

            content = result["messages"][-1].content
            if isinstance(content, list):
                text_parts = [
                    item["text"] for item in content
                    if isinstance(item, dict) and "text" in item
                ]
                return "\n".join(text_parts) if text_parts else str(content)
            return str(content)

        except Exception as e:
            last_error = e
            err_msg = str(e).lower()
            if "429" in err_msg or "resource_exhausted" in err_msg or "404" in err_msg or "not_found" in err_msg:
                # Try next model in sequence
                continue
            else:
                break

    if last_error and ("429" in str(last_error).lower() or "resource_exhausted" in str(last_error).lower()):
        return (
            "⚠️ Google Gemini API Rate Limit / Quota Exceeded (Free Tier limit reached). "
            "Please wait 30-60 seconds before trying again, or upgrade your Gemini API key quota."
        )

    return f"Unable to process request at this time: {str(last_error)}"