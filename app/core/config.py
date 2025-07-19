from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_PREFIX: str
    DEBUG: bool = False

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REDIS_URL: str
    CACHE_TTL: int = 300

    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()