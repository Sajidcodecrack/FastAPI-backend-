from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str
    JWT_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
