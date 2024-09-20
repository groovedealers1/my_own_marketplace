from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
