from typing import Annotated
from fastapi import APIRouter, Depends

from backend.repositories.EntityRepositories import EntityRepositories
from backend.schemas.EntitySchemas import Entity, EntityAdd
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_async_session


entity_router = APIRouter(
    prefix="/api/v1",
    tags=["Entity"]
)


@entity_router.get("/entity")
async def get_entity(session: AsyncSession = Depends(get_async_session)):
    """Get entity."""
    result = await EntityRepositories.get_entity(session)
    return result

@entity_router.post("/entity")
async def post_entity(entity: Annotated[EntityAdd, Depends()], session: AsyncSession = Depends(get_async_session)):
    """Post entity."""
    result =  await EntityRepositories.post_entity(entity, session)
    return result
