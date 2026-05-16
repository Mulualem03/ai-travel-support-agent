from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.booking_schema import BookingResponse
from app.services.booking_service import get_booking_by_reference

router = APIRouter()


@router.get("/{booking_reference}", response_model=BookingResponse)
def get_booking(booking_reference: str, db: Session = Depends(get_db)):
    booking = get_booking_by_reference(db, booking_reference)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
