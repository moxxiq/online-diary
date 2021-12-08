from app.core.schemas.subjects import Subject
from app.db import database
from app.core.models.subjects import subjects


async def post(payload: Subject):
    query = subjects.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = subjects.select().where(id == subjects.c.id)
    return await database.fetch_one(query=query)
