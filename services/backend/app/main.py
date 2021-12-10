from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import all as v1_endpoints
from app.db import database
from app.misc.utils import create_admin_if_not_exists

app = FastAPI()
v1 = FastAPI()

origins = [
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    await database.connect()
    await create_admin_if_not_exists()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


v1.include_router(v1_endpoints)

app.mount("/api/v1", v1)