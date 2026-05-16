from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.ticket import SupportTicket

router = APIRouter()


@router.get("/dashboard/metrics")
def dashboard_metrics(db: Session = Depends(get_db)):
    total_conversations = db.query(Conversation).count()
    total_messages = db.query(Message).count()
    open_tickets = db.query(SupportTicket).filter(SupportTicket.status == "open").count()
    resolved_tickets = db.query(SupportTicket).filter(SupportTicket.status == "resolved").count()

    return {
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "open_tickets": open_tickets,
        "resolved_tickets": resolved_tickets,
    }
