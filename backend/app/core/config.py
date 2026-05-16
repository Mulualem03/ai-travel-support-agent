from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Travel Support Agent"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite:///./travel_support.db"
    OPENAI_API_KEY: str | None = None
    JWT_SECRET_KEY: str = "dev-secret"
    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"


settings = Settings()
