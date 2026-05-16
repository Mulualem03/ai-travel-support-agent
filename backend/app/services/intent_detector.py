from dataclasses import dataclass


@dataclass
class IntentResult:
    intent: str
    confidence: float


def detect_intent(message: str) -> IntentResult:
    text = message.lower()

    if "trv-" in text or "booking" in text or "status" in text:
        return IntentResult("booking_status", 0.92)

    if "cancel" in text or "cancellation" in text:
        return IntentResult("cancellation_policy", 0.86)

    if "refund" in text:
        return IntentResult("refund_policy", 0.86)

    if "baggage" in text or "luggage" in text or "bag" in text:
        return IntentResult("baggage_policy", 0.84)

    if "change" in text and "flight" in text:
        return IntentResult("flight_change", 0.84)

    if "human" in text or "agent" in text or "person" in text or "complaint" in text:
        return IntentResult("human_escalation", 0.95)

    return IntentResult("general_policy", 0.65)
