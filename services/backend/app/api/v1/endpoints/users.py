from fastapi import APIRouter, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user
from app.core.schemas.users import User, UserInDB

router = APIRouter()


@router.get("/me", response_model=UserInDB)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/", response_model=UserInDB, status_code=201)
async def create_user(payload: User):
    user = await crud.users.get_by_email(payload.email)
    if user:
        raise HTTPException(status_code=403, detail="User with this email already exists")
    user_id = await crud.users.post(payload)
    response_object = await crud.users.get(user_id)
    return response_object
