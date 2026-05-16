from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.ticket import SupportTicket
from app.schemas.ticket_schema import TicketResponse

router = APIRouter()


@router.get("", response_model=list[TicketResponse])
def list_tickets(db: Session = Depends(get_db)):
    return db.query(SupportTicket).order_by(SupportTicket.created_at.desc()).all()


@router.patch("/{ticket_id}/resolve", response_model=TicketResponse)
def resolve_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(SupportTicket).filter(SupportTicket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    ticket.status = "resolved"
    ticket.resolved_at = datetime.utcnow()
    db.commit()
    db.refresh(ticket)
    return ticket
