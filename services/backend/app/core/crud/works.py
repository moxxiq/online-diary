from app.core.schemas.works import Work, WorkContent
from app.db import database
from app.core.models.works import works
from fastapi.encoders import jsonable_encoder


async def post(payload: Work):
    query = works.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = works.select().where(id == works.c.id)
    return await database.fetch_one(query=query)

async def put(id: int, payload: WorkContent):
    query = (
        works
        .update()
        .where(id == works.c.id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)

async def delete(id: int):
    query = works.delete().where(id == works.c.id)
    return await database.execute(query=query)
