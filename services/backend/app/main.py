from fastapi import FastAPI

from app.api.v1.endpoints import notes, ping
from app.db import engine, database, metadata

metadata.create_all(engine)

app = FastAPI()
v1 = FastAPI()

@v1.on_event("startup")
async def startup():
    await database.connect()


@v1.on_event("shutdown")
async def shutdown():
    await database.disconnect()


v1.include_router(ping.router)
v1.include_router(notes.router, prefix="/notes", tags=["notes"])

app.mount("/api/v1", v1)