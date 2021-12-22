from datetime import datetime

from app.core.schemas.marks import Mark, MarkContent
from app.db import database
from app.core.models.marks import marks
from fastapi.encoders import jsonable_encoder


async def post(payload: Mark):
    query = marks.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = marks.select().where(id == marks.c.id)
    return await database.fetch_one(query=query)

async def put(id: int, payload: Mark):
    payload_dict = payload.dict()
    payload_dict.update(
        {"creation_date": datetime.now().replace(tzinfo=None)})
    query = (
        marks
            .update()
            .where(id == marks.c.id)
            .values(**payload_dict)
    )
    return await database.execute(query=query)

async def patch(id: int, payload: MarkContent):
    payload_dict = payload.dict()
    payload_dict.update(
        {"creation_date": datetime.now().replace(tzinfo=None)})
    query = (
        marks
            .update()
            .where(id == marks.c.id)
            .values(**payload_dict)
    )
    return await database.execute(query=query)

async def delete(id: int):
    query = marks.delete().where(id == marks.c.id)
    return await database.execute(query=query)

async def get_by_work_student(work_id: int, student_id: int):
    query = (
        marks.select().where((work_id == marks.c.work_id) & (student_id == marks.c.student_id))
    )
    return await database.fetch_one(query=query)
