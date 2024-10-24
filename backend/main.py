from fastapi import FastAPI

from backend.api_v1.EntityRouter import entity_router
from backend.database import DATABASE_URL

app = FastAPI()

print(DATABASE_URL)
app.include_router(entity_router)
