from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserWithID
from app.core.schemas.students import Student

router = APIRouter()



@router.post("/students/", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(payload: Student, current_user: UserWithID = Depends(get_current_user_with_scopes([1]))):
    student_in_db = await crud.students.get(payload.user_id)
    if student_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This user is already a student")
    await crud.students.post(payload)
    response_object = await crud.students.get(payload.user_id)
    return response_object

@router.get("/students/{user_id}/", response_model=Student)
async def read_student(user_id: int = Path(..., gt=0), user: UserWithID = Depends(get_current_user)):
    student = await crud.students.get(user_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stuent not found")
    return student

# TODO: create validation scheme to all methods without `response_model`
@router.get("/classes/{class_id}/students/",)
async def get_all_class_students(class_id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    if current_user.get("type") not in [1, 2]: # Teacher -> can view all
        if not await crud.classes.if_student_in_class(student_id=current_user.get(id),
                                                      class_id=class_id):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not allowed to see other classes")
    return await crud.students.get_all_class_students(class_id)

