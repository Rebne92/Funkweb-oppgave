from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env_name: str = "local"
    # Supply a default value (e.g., local SQLite database) to prevent missing field errors
    database_url: str = "sqlite:///./test.db"

    # Pydantic v2 configuration syntax
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
app = FastAPI(title="Production API")

@app.get("/healthz", tags=["System"])
async def health_check():
    return {"status": "healthy", "environment": settings.env_name}