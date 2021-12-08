from app.core.schemas.students import Student
from app.db import database
from app.core.models.students import students


async def post(payload: Student):
    query = students.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(user_id: int):
    query = students.select().where(user_id == students.c.user_id)
    return await database.fetch_one(query=query)
