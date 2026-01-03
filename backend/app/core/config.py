# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_name: str
    env: str
    secret_key: str
    access_token_expire_minutes: int

    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"

settings = Settings()
