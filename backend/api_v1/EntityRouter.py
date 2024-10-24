from typing import Annotated
from fastapi import APIRouter, Depends

from backend.repositories.EntityRepositories import EntityRepositories
from backend.schemas.EntitySchemas import Entity, EntityAdd


entity_router = APIRouter(
    prefix="/api/v1",
    tags=["Entity"]
)


@entity_router.get("/entity")
async def get_entity():
    """Get entity."""
    result = await EntityRepositories.get_entity()
    return result


@entity_router.post("/entity")
async def post_entity(entity: Annotated[EntityAdd, Depends()]):
    """Post entity."""
    result =  await EntityRepositories.post_entity(entity)
    return result
