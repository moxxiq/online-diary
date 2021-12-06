from datetime import date

from app.config import FASTAPI_ADMIN_EMAIL, FASTAPI_ADMIN_PASSWORD

from app.core import crud
from app.core.schemas.users import NewUser

async def create_admin_if_not_exists():
    email = FASTAPI_ADMIN_EMAIL
    password = FASTAPI_ADMIN_PASSWORD
    if not (email and password):
        # Exit if there is no config
        return
    user = await crud.users.get_by_email(email)
    if user:
        print("Admin with this email exists")
        return
    id = await crud.users.post(NewUser(
        email = email,
        password = password,
        type = 1,
        name = 'admin',
        surname = 'admin',
        midname = 'admin',
        birthday = date(2021, 12, 23),
    ))
    print(f"Admin:{id} account created")
