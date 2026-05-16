from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.chat_schema import ChatMessageRequest, ChatMessageResponse
from app.services.ai_agent import run_support_agent

router = APIRouter()


@router.post("/message", response_model=ChatMessageResponse)
def send_message(payload: ChatMessageRequest, db: Session = Depends(get_db)):
    return run_support_agent(
        db=db,
        message=payload.message,
        user_id=payload.user_id,
        conversation_id=payload.conversation_id,
    )
