from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import User
from app.core.schemas.teachers import Teacher

router = APIRouter()



@router.post("/", response_model=Teacher, status_code=status.HTTP_201_CREATED)
async def create_teacher(payload: Teacher, current_user: User = Depends(get_current_user_with_scopes([1]))):
    teacher_in_db = await crud.teachers.get(payload.user_id)
    if teacher_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This user is already a teacher")
    await crud.teachers.post(payload)
    response_object = await crud.teachers.get(payload.user_id)
    return response_object
