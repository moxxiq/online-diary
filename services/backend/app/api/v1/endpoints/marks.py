from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserWithID
from app.core.schemas.marks import Mark, MarkDB

router = APIRouter()

@router.post("/marks/", response_model=MarkDB, status_code=status.HTTP_201_CREATED)
async def create_marks(payload: Mark, current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    # TODO: remove vulnerability so that student could get mark for work of other classes work
    mark_in_db = await crud.marks.get_by_work_student(work_id=payload.work_id, student_id=payload.student_id)
    if mark_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Mark is already set")
    if (current_user.get("type") == 2) and (current_user.get("id") != (await crud.works.get_teacher_of_the_work(payload.work_id)).get("user_id")):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Teacher is not allowed to set the marks for other teacher works")
    mark_id = await crud.marks.post(payload)
    response_object = await crud.marks.get(mark_id)
    return response_object

@router.get("/marks/{id}/", response_model=MarkDB)
async def read_marks(id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    mark_in_db = await crud.marks.get(id)
    if not mark_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mark not set")
    if current_user.get("type") not in [1, 2]:
        if current_user.get("id") != mark_in_db.get("student_id"):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not allowed to see the marks of others")
    if (current_user.get("id") != (await crud.works.get_teacher_of_the_work(mark_in_db.get("work_id"))).get("user_id")) and (current_user.get("type") == 2):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Teacher is not allowed to see the marks of other teachers")
    return mark_in_db

@router.delete("/marks/{id}/", response_model=MarkDB)
async def delete_marks(id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    mark_in_db = await crud.marks.get(id)
    if not mark_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mark not found")
    if (current_user.get("id") != (await crud.works.get_teacher_of_the_work(mark_in_db.get("work_id"))).get("user_id")) and (current_user.get("type") == 2):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Techer is not allowed to delete the marks of other teachers")
    await crud.marks.delete(id)
    return mark_in_db

@router.get("/works/{work_id}/students/{student_id}/marks/", response_model=MarkDB)
async def read_work_student_marks(work_id: int = Path(..., gt=0), student_id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    mark_in_db = await crud.marks.get_by_work_student(work_id, student_id)
    if not mark_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mark not set")
    if current_user.get("type") not in [1, 2]:
        if current_user.get("id") != mark_in_db.get("student_id"):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not allowed to see the marks of others")
    if (current_user.get("id") != (await crud.works.get_teacher_of_the_work(mark_in_db.get("work_id"))).get("user_id")) and (current_user.get("type") == 2):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Techer is not allowed to see the marks of other teachers")
    return mark_in_db
