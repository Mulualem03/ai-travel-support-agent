# Security Considerations

## Current MVP

The MVP includes placeholder authentication only.

## Production security requirements

1. Use real password hashing with bcrypt.
2. Use JWT access tokens and refresh tokens.
3. Add role-based access control.
4. Validate all user input.
5. Rate-limit chat requests.
6. Store API keys in environment variables.
7. Do not expose LLM provider keys to frontend.
8. Restrict CORS to trusted origins.
9. Log security-sensitive events.
10. Avoid storing sensitive personal data unless required.
11. Add prompt-injection protection for RAG.
12. Use HTTPS in production.

## AI safety

The assistant should:

- Not invent booking details.
- Ask for a booking reference when needed.
- Escalate low-confidence answers.
- Use retrieved policy context for policy answers.
- Avoid making legal guarantees.
