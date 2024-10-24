from fastapi import FastAPI
from backend.api_v1.EntityRouter import entity_router


app = FastAPI()

app.include_router(entity_router)
