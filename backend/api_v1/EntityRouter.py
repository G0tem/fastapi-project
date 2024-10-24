from fastapi import APIRouter

from backend.repositories.EntityRepositories import EntityRepositories


entity_router = APIRouter(
    prefix="/api/v1",
    tags=["Entity"]
)


@entity_router.get("/entity")
async def get_entity():
    """Get entity."""
    result = EntityRepositories.get_entity()
    return result