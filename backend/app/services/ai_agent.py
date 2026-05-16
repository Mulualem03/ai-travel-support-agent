from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message
from app.services.intent_detector import detect_intent
from app.services.booking_service import extract_booking_reference, get_booking_by_reference
from app.services.rag_service import search_policy_chunks, generate_policy_answer
from app.services.ticket_service import create_ticket


def get_or_create_conversation(db: Session, user_id: int, conversation_id: int | None) -> Conversation:
    if conversation_id:
        existing = db.query(Conversation).filter(Conversation.id == conversation_id).first()
        if existing:
            return existing

    conversation = Conversation(user_id=user_id, title="Travel support conversation")
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


def save_message(db: Session, conversation_id: int, sender: str, text: str, intent: str | None = None, confidence: float | None = None):
    msg = Message(
        conversation_id=conversation_id,
        sender=sender,
        message_text=text,
        intent=intent,
        confidence=confidence,
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def run_support_agent(db: Session, message: str, user_id: int, conversation_id: int | None = None) -> dict:
    conversation = get_or_create_conversation(db, user_id, conversation_id)
    intent_result = detect_intent(message)

    save_message(
        db=db,
        conversation_id=conversation.id,
        sender="user",
        text=message,
        intent=intent_result.intent,
        confidence=intent_result.confidence,
    )

    used_tools = []
    escalated = False

    if intent_result.intent == "booking_status":
        used_tools.append("booking_lookup")
        ref = extract_booking_reference(message)

        if not ref:
            response = "Please provide your booking reference, for example TRV-10234, so I can check your booking status."
        else:
            booking = get_booking_by_reference(db, ref)
            if not booking:
                response = f"I could not find booking {ref}. I have created a support ticket for a human agent to review."
                create_ticket(db, conversation.id, user_id, "booking_not_found", f"Booking reference {ref} was not found.")
                escalated = True
            else:
                response = (
                    f"Your booking {booking.booking_reference} is {booking.booking_status}. "
                    f"Destination: {booking.destination}. "
                    f"Travel dates: {booking.departure_date} to {booking.return_date}. "
                    f"Flight status: {booking.flight_status}. "
                    f"Hotel: {booking.hotel_name}, hotel status: {booking.hotel_status}. "
                    f"Total price: £{float(booking.total_price):.2f}."
                )

    elif intent_result.intent == "human_escalation":
        used_tools.append("escalation_tool")
        ticket = create_ticket(
            db,
            conversation.id,
            user_id,
            "human_requested",
            f"Customer requested human support: {message}",
            priority="normal",
        )
        escalated = True
        response = f"I have created support ticket #{ticket.id}. A human support agent can now review your request."

    else:
        used_tools.append("policy_rag_search")
        chunks = search_policy_chunks(db, message)
        response = generate_policy_answer(message, chunks)

        if intent_result.confidence < 0.7 or "could not find" in response.lower():
            used_tools.append("escalation_tool")
            create_ticket(
                db,
                conversation.id,
                user_id,
                "low_confidence_policy_answer",
                f"Low-confidence answer for user question: {message}",
            )
            escalated = True

    save_message(
        db=db,
        conversation_id=conversation.id,
        sender="assistant",
        text=response,
        intent=intent_result.intent,
        confidence=intent_result.confidence,
    )

    return {
        "conversation_id": conversation.id,
        "intent": intent_result.intent,
        "response": response,
        "used_tools": used_tools,
        "confidence": intent_result.confidence,
        "escalated": escalated,
    }
