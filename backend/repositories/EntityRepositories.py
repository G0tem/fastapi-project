from backend.models.EntityModel import Entity
from sqlalchemy import select
from backend.database import async_session, get_async_session


class EntityRepositories:
    """Class for entity repositories."""
    
    async def get_entity():
        async for session in get_async_session():
            entities = await session.execute(
                select(Entity).order_by(Entity.id)
            )
            return [
                {
                    "id": entity.id,
                    "name": entity.name,
                    "description": entity.description,
                }
                for entity in entities.scalars().all()
            ]

    async def post_entity(entity):
        async with async_session() as session:
            new_entity = Entity(
                name=entity.name,
                description=entity.description,
            )
            session.add(new_entity)
            await session.commit()
            await session.refresh(new_entity)
            return {
                "id": new_entity.id,
                "name": new_entity.name,
                "description": new_entity.description,
            }
