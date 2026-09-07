from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from models.job_model import Base
import pytest
from fastapi.testclient import TestClient
from core.db import get_db
from main import app





engine = create_async_engine("sqlite+aiosqlite:///:memory:")
session_maker = async_sessionmaker(engine)





async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




async def override_get_db():
    async with session_maker() as session:
        yield session


@pytest.fixture
async def test_client():
    await create_tables()
    client = TestClient(app)
    app.dependency_overrides[get_db] = override_get_db
    yield client
    app.dependency_overrides.clear()








