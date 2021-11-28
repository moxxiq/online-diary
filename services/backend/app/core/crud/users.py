from app.core.schemas.users import UserSchema
from app.db import users, database

async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)

async def get_by_email(email: str):
    query = users.select().where(email == users.c.email)
    return await database.fetch_one(query=query)
