from . import (
    notes,
    ping,
    authorization,
    users,
    teachers,
)

from fastapi import APIRouter

all = APIRouter()

all.include_router(ping.router)
all.include_router(notes.router, prefix="/notes", tags=["notes"])
all.include_router(authorization.router, prefix="/auth", tags=["auth"])
all.include_router(users.router, prefix="/users", tags=["users"])
all.include_router(teachers.router, prefix="/teachers", tags=["teachers"])