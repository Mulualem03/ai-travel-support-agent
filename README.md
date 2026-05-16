# AI Travel Customer Support Agent

A full-stack AI-powered customer support platform for a travel company, built with **React**, **FastAPI**, **PostgreSQL**, **RAG**, and **agent-style tool calling**.

## What this project demonstrates

This project is designed for an AI Developer portfolio and demonstrates:

- Full-stack AI application development
- Python FastAPI backend
- React frontend
- REST API design
- LLM integration architecture
- RAG over travel policy documents
- Agent routing and tool calling
- Mock booking lookup tool
- Human escalation workflow
- Conversation history
- Admin dashboard design
- PostgreSQL database modeling
- Docker-based local development
- Production-oriented documentation

## Main use cases

Customers can ask:

- "What is the status of booking TRV-10234?"
- "Can I cancel my hotel?"
- "What is the baggage allowance?"
- "Can I change my flight date?"
- "Can I get a refund?"
- "I want to speak to a human agent."

The AI agent decides whether to:

1. Answer from policy documents using RAG.
2. Look up booking data using a tool.
3. Create a support ticket for human escalation.
4. Ask for missing information.

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite |
| Backend | Python FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Auth | JWT-ready placeholder |
| AI | LLM integration-ready service layer |
| RAG | Keyword-based MVP retrieval, upgradeable to pgvector/Chroma |
| Deployment | Docker + Docker Compose |

## Repository structure

```text
ai-travel-support-agent/
├── backend/
├── frontend/
├── docs/
├── data/
├── docker-compose.yml
├── .env.example
└── README.md
```

## Quick start

### 1. Copy environment file

```bash
cp .env.example .env
```

### 2. Start services

```bash
docker compose up --build
```

### 3. Backend

FastAPI runs at:

```text
http://localhost:8000
```

API docs:

```text
http://localhost:8000/docs
```

### 4. Frontend

React runs at:

```text
http://localhost:5173
```

## Demo accounts

The MVP uses simple mock users in the seed layer.

Recommended demo users:

| Role | Email | Password |
|---|---|---|
| Customer | customer@example.com | password123 |
| Admin | admin@example.com | password123 |

## Key backend endpoints

```text
GET  /health
POST /chat/message
GET  /bookings/{booking_reference}
GET  /admin/dashboard/metrics
GET  /tickets
PATCH /tickets/{ticket_id}/resolve
```

## Example request

```bash
curl -X POST http://localhost:8000/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message":"What is the status of booking TRV-10234?","conversation_id":1,"user_id":1}'
```

## Example response

```json
{
  "conversation_id": 1,
  "intent": "booking_status",
  "response": "Your booking TRV-10234 is confirmed...",
  "used_tools": ["booking_lookup"],
  "confidence": 0.92,
  "escalated": false
}
```

## Documentation

See the `/docs` folder:

- `architecture.md`
- `api-documentation.md`
- `ai-workflow.md`
- `database-design.md`
- `deployment-guide.md`
- `demo-script.md`
- `deliverables-checklist.md`
- `requirements.md`
- `testing-strategy.md`
- `security.md`

## Future improvements

- Replace keyword retrieval with pgvector or Chroma.
- Add real OpenAI or Azure OpenAI integration.
- Add JWT authentication fully.
- Add streaming responses with Server-Sent Events.
- Add tests for all services.
- Deploy frontend and backend separately.
- Add CI/CD pipeline.
