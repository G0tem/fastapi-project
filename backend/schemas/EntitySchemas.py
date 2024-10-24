from pydantic import BaseModel


class Entity(BaseModel):

    id: int
    name: str
    description: str | None = None

    
class EntityAdd(BaseModel):

   name: str
   description: str | None = None