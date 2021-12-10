from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import User
from app.core.schemas.workplaces import Workplace, WorkplaceDB

router = APIRouter()

@router.post("workplaces/", response_model=WorkplaceDB, status_code=status.HTTP_201_CREATED)
async def create_workplace(payload: Workplace, current_user: User = Depends(get_current_user_with_scopes([1, 2]))):
    workplace_in_db = await crud.workplaces.get_by_attrs(payload)
    if workplace_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This workplace is already exists")
    workplace_id = await crud.workplaces.post(payload)
    response_object = await crud.workplaces.get(workplace_id)
    return response_object

@router.get("workplaces/{id}/", response_model=WorkplaceDB)
async def read_workplace(id: int = Path(..., gt=0), user: User = Depends(get_current_user)):
    workplace_in_db = await crud.workplaces.get(id)
    if not workplace_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workplace not found")
    return workplace_in_db

@router.get("/teacher/{user_id}/subject/{subject_id}/class/{class_id}/workplaces", response_model=WorkplaceDB)
async def read_teacher_subject_class_workplace(user_id: int = Path(..., gt=0),
                                               subject_id: int = Path(..., gt=0),
                                               class_id: int = Path(..., gt=0)):
    pass  # TODO: finish this
