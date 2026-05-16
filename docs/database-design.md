# Database Design

## Tables

### users

Stores customer and admin accounts.

Fields:
- id
- full_name
- email
- password_hash
- role
- created_at

### bookings

Stores mock travel bookings.

Fields:
- id
- booking_reference
- user_id
- destination
- departure_date
- return_date
- flight_status
- hotel_name
- hotel_status
- total_price
- booking_status

### conversations

Stores support conversations.

Fields:
- id
- user_id
- title
- status
- created_at
- updated_at

### messages

Stores user and assistant messages.

Fields:
- id
- conversation_id
- sender
- message_text
- intent
- confidence
- created_at

### support_tickets

Stores human escalation tickets.

Fields:
- id
- conversation_id
- user_id
- issue_type
- status
- priority
- summary
- created_at
- resolved_at

### documents

Stores policy documents.

Fields:
- id
- title
- category
- content
- created_at

### document_chunks

Stores RAG chunks.

Fields:
- id
- document_id
- chunk_text
- metadata_json
- created_at
