# Testing Strategy

## Backend tests

Test:

- Intent detection
- Booking reference extraction
- Booking lookup
- RAG retrieval
- Ticket creation
- Chat endpoint response shape

## Frontend tests

Test:

- Chat input
- API error display
- Message rendering
- Dashboard metrics rendering

## Integration tests

Test complete workflows:

1. Booking status request.
2. Policy question request.
3. Human escalation request.
4. Ticket resolution.

## AI quality tests

Create a set of evaluation questions:

- Can I cancel my hotel?
- Can I get a refund?
- What baggage is included?
- Can I change my flight?
- What is the status of booking TRV-10234?

Measure:

- Correct intent
- Correct tool used
- Grounded answer
- No invented booking details
- Proper escalation
