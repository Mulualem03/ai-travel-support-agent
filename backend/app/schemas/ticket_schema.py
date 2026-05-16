from pydantic import BaseModel
from datetime import datetime


class TicketResponse(BaseModel):
    id: int
    conversation_id: int
    user_id: int
    issue_type: str
    status: str
    priority: str
    summary: str
    created_at: datetime
    resolved_at: datetime | None

    class Config:
        from_attributes = True
