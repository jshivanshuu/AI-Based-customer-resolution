from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    pnr: str | None = None


class ChatResponse(BaseModel):
    response: str
    pnr: str | None = None