from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import mapped_column

from config import settings
from typing import Annotated


str_256 = Annotated[str, 256]
intpk = Annotated[int, mapped_column(primary_key=True)]


engine = create_async_engine(
    url=f'{settings.DATABASE_URL_asyncpg}',
    echo=False
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
