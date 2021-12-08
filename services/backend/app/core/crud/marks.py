from app.core.schemas.marks import Mark
from app.db import database
from app.core.models.marks import marks
from fastapi.encoders import jsonable_encoder


async def post(payload: Mark):
    query = marks.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = marks.select().where(id == marks.c.id)
    return await database.fetch_one(query=query)
