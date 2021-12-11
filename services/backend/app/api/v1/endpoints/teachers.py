from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserInDB
from app.core.schemas.teachers import Teacher

router = APIRouter()



@router.post("/", response_model=Teacher, status_code=status.HTTP_201_CREATED)
async def create_teacher(payload: Teacher, current_user: UserInDB = Depends(get_current_user_with_scopes([1]))):
    teacher_in_db = await crud.teachers.get(payload.user_id)
    if teacher_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This user is already a teacher")
    await crud.teachers.post(payload)
    response_object = await crud.teachers.get(payload.user_id)
    return response_object

@router.get("/{user_id}/", response_model=Teacher)
async def read_teacher(user_id: int = Path(..., gt=0), user: UserInDB = Depends(get_current_user)):
    teacher = await crud.teachers.get(user_id)
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return teacher
