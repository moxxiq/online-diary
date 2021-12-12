from app.core.schemas.classes import Class
from app.db import database
from app.core.models.classes import classes
from app.core.models.students import students
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

async def if_student_in_class(student_id: int, class_id: int):
    query = (
        students
        .select()
        .where(
         ( (student_id == students.c.user_id) & (class_id == students.c.class_id) ).exists() )
        .scalar()
    )
    return await database.fetch_val(query=query)

async def search_class(class_number: int, class_name: str):
    query = (
        classes
        .select()
        .where(class_number == classes.c.number)
        .where(classes.c.name.contains(class_name))
    )
    return await database.fetch_all(query=query)