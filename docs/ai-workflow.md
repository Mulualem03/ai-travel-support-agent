# AI Workflow

## Agent flow

```text
1. Receive user message
2. Save user message
3. Detect intent
4. Choose tool
5. Retrieve data
6. Generate response
7. Save assistant response
8. Escalate if needed
9. Return response
```

## Supported intents

| Intent | Tool |
|---|---|
| booking_status | booking_lookup |
| cancellation_policy | policy_rag_search |
| refund_policy | policy_rag_search |
| baggage_policy | policy_rag_search |
| flight_change | policy_rag_search |
| human_escalation | escalation_tool |
| general_policy | policy_rag_search |

## Tool calling design

The MVP implements tool calling in Python service functions:

- `get_booking_by_reference()`
- `search_policy_chunks()`
- `create_ticket()`

Production upgrade:
Use LLM tool/function calling with JSON schemas for each tool.
