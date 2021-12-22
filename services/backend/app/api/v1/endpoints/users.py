from fastapi import APIRouter, HTTPException, status, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import User, NewUser, UserWithID

router = APIRouter()


@router.post("/users", response_model=UserWithID, status_code=status.HTTP_201_CREATED)
async def create_user(payload: NewUser, current_user: UserWithID = Depends(get_current_user_with_scopes([1]))):
    user_in_db = await crud.users.get_by_email(payload.email)
    if user_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists")
    user_id = await crud.users.post(payload)
    response_object = await crud.users.get(user_id)
    return response_object

@router.get("/users/me", response_model=UserWithID)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
