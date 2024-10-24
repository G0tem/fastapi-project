from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from backend.config import POSTGRES_HOST, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL)
print(engine)
async_session = async_sessionmaker(engine, expire_on_commit=False)
metadata = MetaData() 
Base = declarative_base()
