from fastapi import APIRouter, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user
from app.core.schemas.users import UserSchema

router = APIRouter()


@router.post("/me", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_user)):
    return current_user
