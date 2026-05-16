from datetime import date
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.user import User
from app.models.booking import Booking
from app.models.document import Document, DocumentChunk


POLICIES = [
    {
        "title": "Cancellation Policy",
        "category": "cancellation",
        "content": "Hotel cancellations made more than 48 hours before check-in may qualify for a partial refund. Cancellations within 48 hours of check-in may incur cancellation fees. Flight cancellation terms depend on fare type and airline rules."
    },
    {
        "title": "Refund Policy",
        "category": "refund",
        "content": "Refunds are processed to the original payment method. Eligible refunds usually take 5 to 10 business days. Non-refundable bookings may only qualify for taxes or fees refunds."
    },
    {
        "title": "Baggage Policy",
        "category": "baggage",
        "content": "Standard economy flight bookings include one cabin bag up to 7kg. Checked baggage allowance depends on airline and fare type. Extra baggage can be purchased before departure."
    },
    {
        "title": "Flight Change Policy",
        "category": "flight_change",
        "content": "Flight date changes may be requested before departure. Change fees and fare differences may apply. Some promotional fares do not allow date changes."
    },
    {
        "title": "Visa and Travel Documents",
        "category": "visa",
        "content": "Customers are responsible for valid passports, visas, and entry requirements. Passport validity of at least six months may be required for some destinations."
    },
]


def seed_demo_data():
    db: Session = SessionLocal()

    try:
        if db.query(User).count() == 0:
            customer = User(
                full_name="Demo Customer",
                email="customer@example.com",
                password_hash="not-for-production",
                role="customer",
            )
            admin = User(
                full_name="Demo Admin",
                email="admin@example.com",
                password_hash="not-for-production",
                role="admin",
            )
            db.add_all([customer, admin])
            db.commit()

        if db.query(Booking).count() == 0:
            bookings = [
                Booking(
                    booking_reference="TRV-10234",
                    user_id=1,
                    destination="Barcelona",
                    departure_date=date(2026, 6, 20),
                    return_date=date(2026, 6, 25),
                    flight_status="confirmed",
                    hotel_name="Barcelona Central Hotel",
                    hotel_status="confirmed",
                    total_price=1249.00,
                    booking_status="confirmed",
                ),
                Booking(
                    booking_reference="TRV-20456",
                    user_id=1,
                    destination="Rome",
                    departure_date=date(2026, 8, 5),
                    return_date=date(2026, 8, 10),
                    flight_status="pending airline confirmation",
                    hotel_name="Roma Garden Suites",
                    hotel_status="confirmed",
                    total_price=1580.00,
                    booking_status="pending",
                ),
            ]
            db.add_all(bookings)
            db.commit()

        if db.query(Document).count() == 0:
            for policy in POLICIES:
                doc = Document(**policy)
                db.add(doc)
                db.commit()
                db.refresh(doc)

                # MVP chunking: one chunk per policy.
                chunk = DocumentChunk(
                    document_id=doc.id,
                    chunk_text=policy["content"],
                    metadata_json=f'{{"category":"{policy["category"]}"}}',
                )
                db.add(chunk)
            db.commit()
    finally:
        db.close()
