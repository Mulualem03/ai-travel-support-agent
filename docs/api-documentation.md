# API Documentation

## Health

### GET /health

Returns service status.

## Chat

### POST /chat/message

Request:

```json
{
  "message": "What is the status of booking TRV-10234?",
  "user_id": 1,
  "conversation_id": null
}
```

Response:

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

## Bookings

### GET /bookings/{booking_reference}

Returns booking details.

## Tickets

### GET /tickets

Returns support tickets.

### PATCH /tickets/{ticket_id}/resolve

Marks a support ticket as resolved.

## Admin

### GET /admin/dashboard/metrics

Returns operational metrics.

## Documents

### GET /documents

Returns stored policy documents.
