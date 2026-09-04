from pydantic import BaseSettings
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    db_url :