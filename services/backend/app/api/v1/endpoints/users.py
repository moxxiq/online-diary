from fastapi import APIRouter, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import User, NewUser, UserInDB

router = APIRouter()



@router.post("/", response_model=UserInDB, status_code=201)
async def create_user(payload: NewUser, current_user: User = Depends(get_current_user_with_scopes([1]))):
    user_in_db = await crud.users.get_by_email(payload.email)
    if user_in_db:
        raise HTTPException(status_code=403, detail="User with this email already exists")
    user_id = await crud.users.post(payload)
    response_object = await crud.users.get(user_id)
    return response_object

@router.get("/me", response_model=UserInDB)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
