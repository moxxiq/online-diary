from app.core.schemas.users import UserSchema
from app.db import users, database
from app.core.authorization import verify_password

async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)

async def get_by_email(email: str):
    query = users.select().where(email == users.c.email)
    return await database.fetch_one(query=query)

async def authenticate_user(email: str, password: str):
    user = await get_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
