from fastapi import HTTPException
from backend.models.EntityModel import Entity
from sqlalchemy import select
from backend.schemas.EntitySchemas import EntityAdd


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

    async def update_entity(id: int, entity: EntityAdd, session):
        entity_to_update = await session.get(Entity, id)
        if entity_to_update is None:
            raise HTTPException(status_code=404, detail=f"нет обьекта с {id}, изменить невозможно")
        entity_to_update.name = entity.name
        entity_to_update.description = entity.description
        await session.commit()
        await session.refresh(entity_to_update)
        return {
            "id": entity_to_update.id,
            "name": entity_to_update.name,
            "description": entity_to_update.description,
        }

    async def delete_entity(id: int, session):
        entity_to_delete = await session.get(Entity, id)
        if entity_to_delete is None:
            raise HTTPException(status_code=404, detail=f"нет обьекта с {id}, удалить невозможно")
        await session.delete(entity_to_delete)
        await session.commit()
        return {"message": "Entity deleted"}
       