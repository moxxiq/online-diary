from app.core.schemas.classes import Class
from app.db import database
from app.core.models.classes import classes
from fastapi.encoders import jsonable_encoder


async def post(payload: Class):
    query = classes.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = classes.select().where(id == classes.c.id)
    return await database.fetch_one(query=query)

async def get_by_attrs(payload: Class):
    query = classes.select().where((payload.name == classes.c.name) & (payload.number == classes.c.number))
    return await database.fetch_one(query=query)
