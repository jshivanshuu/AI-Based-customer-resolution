from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agent.schemas import ChatRequest, ChatResponse
from agent.agent import run_agent


app = FastAPI(
    title="Customer Resolution Agent",
    description="AI-powered airline disruption resolution agent",
    version="1.0.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Customer Resolution Agent API is running"
    }


# --------------------------------------------------
# Chat Endpoint
# --------------------------------------------------

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    response = run_agent(
        message=request.message,
        pnr=request.pnr
    )

    return ChatResponse(
        response=response,
        pnr=request.pnr
    )