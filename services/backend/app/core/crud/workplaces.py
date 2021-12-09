from app.core.schemas.workplaces import Workplace
from app.db import database
from app.core.models.workplaces import workplaces


async def post(payload: Workplace):
    query = workplaces.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = workplaces.select().where(id == workplaces.c.id)
    return await database.fetch_one(query=query)

async def get_by_attrs(payload: Workplace):
    query = (workplaces
             .select()
             .where(
                 (payload.class_id == workplaces.c.class_id)
                 & (payload.subject_id == workplaces.c.subject_id)
                 & (payload.teacher_id == workplaces.c.teacher_id)
             )
    )
    return await database.fetch_one(query=query)
