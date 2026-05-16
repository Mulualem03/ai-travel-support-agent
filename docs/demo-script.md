# Demo Script

## 1. Introduction

"This is an AI-powered travel customer support platform. It combines a React frontend, FastAPI backend, PostgreSQL database, RAG over travel policy documents, and agent-style tool calling."

## 2. Booking lookup demo

Ask:

```text
What is the status of booking TRV-10234?
```

Expected result:
The AI detects `booking_status`, calls the booking lookup tool, and returns booking details.

## 3. Policy RAG demo

Ask:

```text
Can I cancel my hotel?
```

Expected result:
The AI detects a cancellation policy question, searches travel policy documents, and answers from retrieved policy content.

## 4. Human escalation demo

Ask:

```text
I want to speak to a human agent
```

Expected result:
The AI creates a support ticket and shows it in the admin metrics.

## 5. Admin dashboard

Show:

- total conversations
- total messages
- open tickets
- resolved tickets

## Interview explanation

"I designed this project to show production-style AI engineering. The AI agent routes messages to tools, avoids inventing booking data, uses retrieval for policy answers, and escalates when confidence is low."
