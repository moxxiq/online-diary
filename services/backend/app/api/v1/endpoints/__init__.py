from . import notes, ping

from fastapi import APIRouter

all = APIRouter()

all.include_router(ping.router)
all.include_router(notes.router, prefix="/notes", tags=["notes"])