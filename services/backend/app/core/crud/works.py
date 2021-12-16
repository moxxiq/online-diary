from app.core.schemas.works import Work, WorkContent
from app.db import database
from app.core.models.works import works
from app.core.models.workplaces import workplaces
from app.core.models.users import users
from app.core.models.teachers import teachers
from app.core.models.students import students
from app.core.models.classes import classes
from app.core.models.marks import marks
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

async def get_teacher_of_the_work(work_id: int):
    query = (
        sa.select(teachers.c.user_id, teachers.c.position, )
            .select_from(workplaces
                         .join(works, workplaces.c.id == works.c.workplace_id)
                         .join(teachers, teachers.c.user_id == workplaces.c.teacher_id))
            .where((work_id == works.c.id))
    )
    return await database.fetch_one(query=query)

async def get_all_workplace_teacher_works_marked(workplace_id):
    works_by_workplace = await get_all_workplace_works(workplace_id)
    for work in works_by_workplace:
        query = (
            sa.select(marks.c.id.label("mark_id"), marks.c.creation_date, marks.c.comment, marks.c.mark,
                      students.c.user_id.label("student_id"),
                      users.c.surname, users.c.name, users.c.midname,
                     )
                .select_from(workplaces
                             .join(classes, workplaces.c.class_id == classes.c.id)
                             .join(students, classes.c.id == students.c.class_id)
                             .join(marks, (students.c.user_id == marks.c.student_id), isouter=True)
                             .join(users, students.c.user_id == users.c.id)
                             )
                .where((workplace_id == workplaces.c.id)
                        & (work.get("id") == marks.c.work_id)
                       )
        )
        marks_and_details = await database.fetch_all(query=query)
        yield dict(**dict(work), marks=marks_and_details)


async def get_all_workplace_student_works_marked(workplace_id, student_id):
    works_by_workplace = await get_all_workplace_works(workplace_id)
    for work in works_by_workplace:
        query = (
            marks
            .select()
            .where(
                (marks.c.student_id == student_id)
                & (marks.c.work_id == work.get("id"))
            )
        )
        marks_and_details = await database.fetch_all(query=query)
        yield dict(**dict(work), marks=marks_and_details)
