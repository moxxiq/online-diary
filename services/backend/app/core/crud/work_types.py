from app.core.schemas.work_types import WorkType
from app.db import database
from app.core.models.work_types import work_types


async def post(payload: WorkType):
    query = work_types.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(id: int):
    query = work_types.select().where(id == work_types.c.id)
    return await database.fetch_one(query=query)
