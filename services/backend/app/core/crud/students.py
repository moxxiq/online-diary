from app.core.schemas.students import Student
from app.db import database
from app.core.models.students import students
from app.core.models.users import users

import sqlalchemy as sa

async def post(payload: Student):
    query = students.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get(user_id: int):
    query = students.select().where(user_id == students.c.user_id)
    return await database.fetch_one(query=query)

async def get_all_class_students(class_id: int):
    query = (
        sa.select(users.c.id, users.c.email, users.c.name, users.c.surname, users.c.midname,)
        .select_from(students
                     .join(users, students.c.user_id == users.c.id)
                     )
        .where(class_id == students.c.class_id)
    )
    return await database.fetch_all(query=query)