from sqlalchemy import String, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    sender: Mapped[str] = mapped_column(String(30))
    message_text: Mapped[str] = mapped_column(Text)
    intent: Mapped[str | None] = mapped_column(String(80), nullable=True)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
