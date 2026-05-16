# Deployment Guide

## Local Docker deployment

```bash
cp .env.example .env
docker compose up --build
```

## Production deployment plan

### Backend

Deploy FastAPI to:

- Render
- Railway
- Fly.io
- AWS ECS
- Azure Container Apps

### Frontend

Deploy React to:

- Vercel
- Netlify
- S3 + CloudFront

### Database

Use managed PostgreSQL:

- Supabase
- Neon
- AWS RDS
- Azure PostgreSQL

## Environment variables

Required:

- DATABASE_URL
- OPENAI_API_KEY
- JWT_SECRET_KEY
- FRONTEND_URL

## Production checklist

- Replace placeholder auth with real JWT.
- Use HTTPS.
- Configure CORS strictly.
- Add structured logging.
- Add monitoring and alerts.
- Use pgvector or Chroma for semantic RAG.
- Add CI/CD pipeline.
