from app.core.schemas.users import NewUser
from app.db import database
from app.core.models.users import users
from app.core.authorization import get_password_hash

async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)

async def get_all(page=None, per_page=None):
    pass

async def get_by_email(email: str):
    query = users.select().where(email.lower() == users.c.email)
    return await database.fetch_one(query=query)

async def post(payload: NewUser):
    query = users.insert().values(
        email=payload.email.lower(),
        hashed_password=get_password_hash(payload.password),
        type=payload.type,
        name=payload.name,
        surname=payload.surname,
        midname=payload.midname,
        birthday=payload.birthday,
    )
    return await database.execute(query=query)