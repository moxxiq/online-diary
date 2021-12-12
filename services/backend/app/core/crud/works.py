from app.core.schemas.works import Work, WorkContent
from app.db import database
from app.core.models.works import works
from app.core.models.workplaces import workplaces
from fastapi.encoders import jsonable_encoder

import sqlalchemy as sa

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

async def get_all_workplace_works(workplace_id: int):
    query = (
        works
        .select()
        .where(workplace_id == works.c.workplace_id)
    )
    return await database.fetch_all(query=query)

async def get_all_workplace_work_type_works(workplace_id: int, work_type_id: int):
    query = (
        works
        .select()
        .where((workplace_id == works.c.workplace_id)
               & (work_type_id == works.c.work_type_id))
    )
    return await database.fetch_all(query=query)

async def get_all_class_work_type_works(class_id: int, work_type_id: int):
    query = (
        sa.select(works.c.id, works.c.workplace_id, works.c.work_type_id, works.c.deadline,
                  works.c.headline, works.c.description, works.c.creation_date,
                  workplaces.c.class_id)
        .select_from(workplaces
                     .join(works, workplaces.c.id == works.c.workplace_id))
        .where((class_id == workplaces.c.class_id)
               & (work_type_id == works.c.work_type_id))
    )
    return await database.fetch_all(query=query)
