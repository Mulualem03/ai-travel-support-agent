from sqlalchemy.orm import Session
from app.models.ticket import SupportTicket


def create_ticket(
    db: Session,
    conversation_id: int,
    user_id: int,
    issue_type: str,
    summary: str,
    priority: str = "normal",
) -> SupportTicket:
    ticket = SupportTicket(
        conversation_id=conversation_id,
        user_id=user_id,
        issue_type=issue_type,
        summary=summary,
        priority=priority,
        status="open",
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
