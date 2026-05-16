from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    message: str
    user_id: int = 1
    conversation_id: int | None = None


class ChatMessageResponse(BaseModel):
    conversation_id: int
    intent: str
    response: str
    used_tools: list[str]
    confidence: float
    escalated: bool
