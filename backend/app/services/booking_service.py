import re
from sqlalchemy.orm import Session
from app.models.booking import Booking


def extract_booking_reference(message: str) -> str | None:
    match = re.search(r"TRV-\d{5}", message.upper())
    return match.group(0) if match else None


def get_booking_by_reference(db: Session, booking_reference: str) -> Booking | None:
    return (
        db.query(Booking)
        .filter(Booking.booking_reference == booking_reference.upper())
        .first()
    )
