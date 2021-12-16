from . import (
    ping,
    authorization,
    users,
    teachers,
    classes,
    subjects,
    students,
    workplaces,
    work_types,
    works,
    marks,
)

from fastapi import APIRouter

all = APIRouter()

all.include_router(ping.router)
all.include_router(authorization.router, prefix="/auth", tags=["Auth"])
all.include_router(users.router, prefix="/users", tags=["Users"])
all.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])
all.include_router(classes.router, prefix="/classes", tags=["Classes"])
all.include_router(students.router, tags=["Students"])
all.include_router(subjects.router, prefix="/subjects", tags=["Subjects"])
all.include_router(workplaces.router, prefix="/workplaces", tags=["Workplaces"])
all.include_router(work_types.router, prefix="/work_types", tags=["Work_types"])
all.include_router(works.router, tags=["Works"])
all.include_router(marks.router, tags=["Marks"])
