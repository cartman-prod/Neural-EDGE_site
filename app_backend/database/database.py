from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app_backend.settings import app_settings


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(app_settings.ASYNC_DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator:
    async with async_sessionmaker() as session:
        yield session