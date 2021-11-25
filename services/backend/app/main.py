from fastapi import FastAPI

from app.api.v1.endpoints import all as v1_endpoints
from app.db import engine, database, metadata

metadata.create_all(engine)

app = FastAPI()
v1 = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


v1.include_router(v1_endpoints)

app.mount("/api/v1", v1)