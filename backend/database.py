from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import MetaData


engine = create_async_engine("postgresql+asyncpg://postgresuser:ada32f24gfDSadgsdasdaFGewrdsc@postgres_db_fastapi:5432/postgres")
async_session = async_sessionmaker(engine, expire_on_commit=False)
metadata = MetaData() 
