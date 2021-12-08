from app.core.schemas.works import Work
from app.db import database
from app.core.models.works import works
from fastapi.encoders import jsonable_encoder


async def post(payload: Work):
    query = works.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = works.select().where(id == works.c.id)
    return await database.fetch_one(query=query)
