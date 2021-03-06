from datetime import datetime, date
from typing import Optional

from app.core.schemas.workplaces import Workplace
from app.db import database
from app.core.models.workplaces import workplaces
from app.core.models.classes import classes
from app.core.models.works import works
from app.core.models.marks import marks
from app.core.models.students import students
from app.core.models.subjects import subjects
from app.core.models.teachers import teachers
from app.core.models.users import users

import sqlalchemy as sa

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

async def get_all_student_workplaces_with_details(student_id: int):
    query = (
        sa.select(users.c.id.label("teacher_id"), users.c.email, users.c.name, users.c.surname, users.c.midname,
                  teachers.c.position.label("teacher_position"),
                  subjects.c.id.label("subject_id"), subjects.c.name.label("subject_name"),
                  classes.c.id.label("class_id"), classes.c.name.label("class_name"), classes.c.number.label("class_number"),
                  workplaces.c.id,
                  )
        .select_from(workplaces
        .join(classes, workplaces.c.class_id == classes.c.id)
        .join(subjects, workplaces.c.subject_id == subjects.c.id)
        .join(teachers, workplaces.c.teacher_id == teachers.c.user_id)
        .join(users, teachers.c.user_id == users.c.id)
        .join(students, classes.c.id == students.c.class_id)
        )
        .where(students.c.user_id == student_id)
    )
    return await database.fetch_all(query=query)

async def get_all_teacher_workplaces_with_details(teacher_id: int):
    query = (
        sa.select(subjects.c.id.label("subject_id"), subjects.c.name.label("subject_name"),
                  classes.c.id.label("class_id"), classes.c.name.label("class_name"), classes.c.number.label("class_number"),
                  workplaces.c.id,
                  )
        .select_from(workplaces
        .join(classes, workplaces.c.class_id == classes.c.id)
        .join(subjects, workplaces.c.subject_id == subjects.c.id)
        .join(teachers, workplaces.c.teacher_id == teachers.c.user_id)
        )
        .where(teachers.c.user_id == teacher_id)
    )
    return await database.fetch_all(query=query)

async def get_all_class_teacher_workspaces(class_id: int, teacher_id: int):
    query = (workplaces
        .select()
        .where(
            (class_id == workplaces.c.class_id)
            & (teacher_id == workplaces.c.teacher_id)
        )
    )
    return await database.fetch_all(query=query)

async def get_workplace_analytics_per_user_with_worktype(
        workplace_id: int,
        work_type_id: Optional[int] = None,
        date_from: Optional[datetime] = datetime.combine(date(year=1970, month=1, day=1), datetime.min.time()).replace(tzinfo=None),
        date_to: Optional[datetime] = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=None),
    ):
    query = (
        sa.select(
            marks.c.student_id,
            sa.func.avg(marks.c.mark).label("average_mark"),
            sa.func.count(marks.c.id).label("mark_count"),
            )
            .select_from(workplaces
                         .join(works, workplaces.c.id == works.c.workplace_id)
                         .join(marks, works.c.id == marks.c.work_id)
                         )
            .where((workplace_id == workplaces.c.id)
                   & (marks.c.creation_date >= date_from)
                   & (marks.c.creation_date <= date_to)
                   & (work_type_id == works.c.work_type_id if work_type_id else True))
            .group_by(marks.c.student_id)
    )
    return await database.fetch_all(query=query)
