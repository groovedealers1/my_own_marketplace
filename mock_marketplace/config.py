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


    @property
    def COOKIE_SECRET(self):
        return 'h0bRQnm7IxHxhE6hjQb4iELE1UB6qrsXuq7z4kakiBgLeQ6njl'


    @property
    def MANAGER_SECRET(self):
        return 'c1Nx1cYR4RGh43FDlCvxunopAIMkxwhSTIuLAyrusng8'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()