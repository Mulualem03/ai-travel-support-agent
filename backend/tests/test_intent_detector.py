from app.services.intent_detector import detect_intent


def test_booking_intent():
    result = detect_intent("What is the status of booking TRV-10234?")
    assert result.intent == "booking_status"


def test_refund_intent():
    result = detect_intent("Can I get a refund?")
    assert result.intent == "refund_policy"


def test_human_escalation_intent():
    result = detect_intent("I want to speak to a human agent")
    assert result.intent == "human_escalation"
