from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings

engine = create_async_engine(settings.db_url)
session_maker = async_sessionmaker(engine)

async def get_db():
    async with session_maker() as session:
        yield session
