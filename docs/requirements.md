# Requirements

## Functional requirements

1. Customers can ask travel support questions in a chat interface.
2. The system detects user intent.
3. The system can answer policy questions using RAG.
4. The system can look up mock booking data by booking reference.
5. The system can create human escalation tickets.
6. Users can view AI responses with clear next steps.
7. Admin users can see dashboard metrics.
8. Admin users can view and resolve tickets.
9. Conversations and messages are persisted.
10. Travel policy documents are stored and searchable.

## Non-functional requirements

1. Backend should expose documented REST APIs.
2. Frontend should be responsive and easy to use.
3. The system should be containerized with Docker.
4. The AI workflow should avoid inventing booking data.
5. Low-confidence responses should escalate to humans.
6. Logs and errors should be traceable.
7. The design should support future production upgrades.
8. Architecture should be documented.
