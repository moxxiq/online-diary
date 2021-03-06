from typing import Optional
from datetime import date, datetime

from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserWithID
from app.core.schemas.workplaces import Workplace, WorkplaceDB

router = APIRouter()

@router.post("/workplaces", response_model=WorkplaceDB, status_code=status.HTTP_201_CREATED)
async def create_workplace(payload: Workplace, current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    workplace_in_db = await crud.workplaces.get_by_attrs(payload)
    if workplace_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This workplace is already exists")
    workplace_id = await crud.workplaces.post(payload)
    response_object = await crud.workplaces.get(workplace_id)
    return response_object

@router.get("/workplaces/{id}", response_model=WorkplaceDB)
async def read_workplace(id: int = Path(..., gt=0), user: UserWithID = Depends(get_current_user)):
    """
    Get a Workplace. It's the common of teacher, subject, class. Starting point to which tasks connect
    :param id: id of the workplace needed
    :param user: let only authorised users
    :return: Awaitable Workplace with id of the teacher, subject, class
    """
    workplace_in_db = await crud.workplaces.get(id)
    if not workplace_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workplace not found")
    return workplace_in_db

@router.get("/students/{student_id}/workplaces/detailed")
async def get_all_student_workplaces_with_details(student_id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    if current_user.get("type") not in [1, 2]:
        if student_id != current_user.get("id"):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not allowed to see others work")
    return await crud.workplaces.get_all_student_workplaces_with_details(student_id)

@router.get("/teachers/{teacher_id}/workplaces/detailed")
async def get_all_teachers_workplaces_with_details(teacher_id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    return await crud.workplaces.get_all_teacher_workplaces_with_details(teacher_id)

@router.get("/workplaces/{workplace_id}/analytics/avg")
async def get_workplace_analytics_per_user_with_worktype(
        work_type_id: Optional[int] = None,
        date_from: Optional[datetime] = datetime.combine(date(year=1970, month=1, day=1), datetime.min.time()),
        date_to: Optional[datetime] = datetime.combine(date.today(), datetime.min.time()),
        workplace_id: int = Path(..., gt=0),
        current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2])),
    ):
    if current_user.get("type") not in [1, 2]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not allowed to see the analytics of others")
    workplace_in_db = await crud.workplaces.get(workplace_id)
    if not workplace_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workplace not found")

    return await crud.workplaces.get_workplace_analytics_per_user_with_worktype(
        workplace_id=workplace_id,
        work_type_id=work_type_id,
        date_from=date_from.replace(tzinfo=None),
        date_to=date_to.replace(tzinfo=None),
    )


