from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserWithID
from app.core.schemas.workplaces import Workplace, WorkplaceDB

router = APIRouter()

@router.post("/", response_model=WorkplaceDB, status_code=status.HTTP_201_CREATED)
async def create_workplace(payload: Workplace, current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    workplace_in_db = await crud.workplaces.get_by_attrs(payload)
    if workplace_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This workplace is already exists")
    workplace_id = await crud.workplaces.post(payload)
    response_object = await crud.workplaces.get(workplace_id)
    return response_object

@router.get("/{id}/", response_model=WorkplaceDB)
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

@router.get("/students/{student_id}/workplaces/detailed/")
async def get_all_student_workplaces_with_details(student_id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    if current_user.get("type") not in [1, 2]:
        if student_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not allowed to see others work")
    return await crud.workplaces.get_all_student_workplaces_with_details(student_id)
