from backend.models.EntityModel import Entity
from sqlalchemy import select


class EntityRepositories:
    """Class for entity repositories."""

    async def get_entity(session):
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

    async def post_entity(entity, session):
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

    # async def put_entity(id: int, entity: EntityAdd):
    #     async with async_session() as session:
    #         entity_to_update = await session.get(Entity, id)
    #         if entity_to_update is None:
    #             return {"error": "Entity not found"}
    #         entity_to_update.name = entity.name
    #         entity_to_update.description = entity.description
    #         await session.commit()
    #         await session.refresh(entity_to_update)
    #         return {
    #             "id": entity_to_update.id,
    #             "name": entity_to_update.name,
    #             "description": entity_to_update.description,
    #         }

    # async def delete_entity(id: int):
    #     async with async_session() as session:
    #         entity_to_delete = await session.get(Entity, id)
    #         if entity_to_delete is None:
    #             return {"error": "Entity not found"}
    #         await session.delete(entity_to_delete)
    #         await session.commit()
    #         return {"message": "Entity deleted"}
        