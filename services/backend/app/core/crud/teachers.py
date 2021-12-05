from app.core.schemas.teachers import Teacher
from app.db import database
from app.core.models.teachers import teachers


async def post(payload: Teacher):
    query = teachers.insert().values(
        id=payload.id,
        position=payload.position,
    )
    return await database.execute(query=query)

async def get(id: int):
    query = teachers.select().where(id == teachers.c.user_id)
    return await database.fetch_one(query=query)