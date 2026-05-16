# Architecture

## High-level architecture

```text
Customer/Admin
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
AI Agent Router
   ├── Intent Detector
   ├── Booking Lookup Tool
   ├── Policy RAG Search Tool
   └── Escalation Tool
   ↓
PostgreSQL Database
```

## Core backend components

- `api/`: REST endpoints.
- `models/`: SQLAlchemy database models.
- `schemas/`: Pydantic request/response schemas.
- `services/`: business logic, AI agent, RAG, booking lookup, ticket creation.
- `prompts/`: prompt templates for future LLM integration.
- `seed/`: demo data.

## Design decisions

The MVP uses a deterministic agent workflow with keyword intent detection and keyword-based RAG. This keeps the project buildable for one developer while showing clear upgrade paths to:

- OpenAI function calling
- LangGraph agent orchestration
- pgvector semantic search
- Server-Sent Events streaming
- JWT role-based authentication
