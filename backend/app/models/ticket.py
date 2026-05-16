from sqlalchemy import String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.core.database import Base


class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    issue_type: Mapped[str] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(40), default="open")
    priority: Mapped[str] = mapped_column(String(40), default="normal")
    summary: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
