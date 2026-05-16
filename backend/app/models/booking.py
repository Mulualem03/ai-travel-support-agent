from sqlalchemy import String, Date, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from app.core.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    booking_reference: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    destination: Mapped[str] = mapped_column(String(120))
    departure_date: Mapped[date] = mapped_column(Date)
    return_date: Mapped[date] = mapped_column(Date)
    flight_status: Mapped[str] = mapped_column(String(60))
    hotel_name: Mapped[str] = mapped_column(String(120))
    hotel_status: Mapped[str] = mapped_column(String(60))
    total_price: Mapped[float] = mapped_column(Numeric(10, 2))
    booking_status: Mapped[str] = mapped_column(String(60))
