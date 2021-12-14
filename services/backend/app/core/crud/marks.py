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

async def delete(id: int):
    query = marks.delete().where(id == marks.c.id)
    return await database.execute(query=query)

async def get_by_work_student(work_id: int, student_id: int):
    query = (
        marks.select().where((work_id == marks.c.work_id) & (student_id == marks.c.student_id))
    )
    return await database.fetch_one(query=query)
