from pydantic import Field
from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    db_url : str=Field(alias="SUPABASE_CONNECTION_STRING")

    @property
    def sync_db_url(self) -> str:
        return self.db_url.replace("asyncpg", "psycopg2")

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra='ignore'
    )



settings = Settings()

