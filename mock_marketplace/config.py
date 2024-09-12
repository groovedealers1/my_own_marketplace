# from dotenv import load_dotenv
# import os

# load_dotenv()

# DB_HOST = os.environ.get("DB_HOST")
# DB_PORT = os.environ.get("DB_PORT")
# DB_USER = os.environ.get("DB_USER")
# DB_NAME = os.environ.get("DB_NAME")
# DB_PASS = os.environ.get("DB_PASS")
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()