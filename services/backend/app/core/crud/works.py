from app.core.schemas.works import Work, WorkContent
from app.db import database
from app.core.models.works import works
from fastapi.encoders import jsonable_encoder


async def post(payload: Work):
    payload_dict = payload.dict()
    payload_dict.update(
        {"deadline": payload_dict["deadline"].replace(tzinfo=None) if payload_dict.get("deadline") else None})
    query = works.insert().values(**payload_dict)
    return await database.execute(query=query)

async def get(id: int):
    query = works.select().where(id == works.c.id)
    return await database.fetch_one(query=query)

async def put(id: int, payload: WorkContent):
    payload_dict = payload.dict()
    payload_dict.update(
        {"deadline": payload_dict["deadline"].replace(tzinfo=None) if payload_dict.get("deadline") else None})
    query = (
        works
        .update()
        .where(id == works.c.id)
        .values(**payload_dict)
    )
    return await database.execute(query=query)

async def delete(id: int):
    query = works.delete().where(id == works.c.id)
    return await database.execute(query=query)
