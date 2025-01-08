from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from contextlib import asynccontextmanager

from src.database.db_models.base_model import Model



SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///:tasks.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')