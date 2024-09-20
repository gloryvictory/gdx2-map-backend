from sqlalchemy import MetaData, NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.cfg import DB_DSN, DB_SCHEMA, CONVENTION

# f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

metadata = MetaData(schema=DB_SCHEMA, naming_convention=CONVENTION)
engine = create_async_engine(DB_DSN, poolclass=NullPool, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

print(DB_DSN)

class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session


def pg_async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper
