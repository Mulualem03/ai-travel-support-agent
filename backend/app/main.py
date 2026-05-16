from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import chat, bookings, tickets, admin, documents, auth
from app.core.config import settings
from app.core.database import Base, engine
from app.seed.seed_data import seed_demo_data

Base.metadata.create_all(bind=engine)
seed_demo_data()

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Travel Customer Support Agent API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
app.include_router(tickets.router, prefix="/tickets", tags=["tickets"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])

@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.APP_NAME}
