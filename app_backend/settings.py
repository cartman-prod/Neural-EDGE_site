import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    class Config:
        env_file = os.path.join(os.path.dirname(__file__), ".env")
    
# DB parameters
    DB_HOST: str
    DB_PORT: str | int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_DRIVER_SYNC: str
    DB_DRIVER_ASYNC: str
    
    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+{self.DB_DRIVER_ASYNC}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def SYNC_DATABASE_URL(self):
        return f"postgresql+{self.DB_DRIVER_SYNC}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


app_settings = Settings()