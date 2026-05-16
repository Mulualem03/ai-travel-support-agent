from pydantic import BaseModel
from datetime import date


class BookingResponse(BaseModel):
    booking_reference: str
    destination: str
    departure_date: date
    return_date: date
    flight_status: str
    hotel_name: str
    hotel_status: str
    total_price: float
    booking_status: str

    class Config:
        from_attributes = True
