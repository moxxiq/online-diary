from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import User
from app.core.schemas.work_types import WorkType, WorkTypeDB

router = APIRouter()



@router.post("/", response_model=WorkTypeDB, status_code=status.HTTP_201_CREATED)
async def create_work_type(payload: WorkType, current_user: User = Depends(get_current_user_with_scopes([1, 2]))):
    work_type_in_db = await crud.work_types.get_by_attrs(payload)
    if work_type_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This work_type is already exists")
    work_type_id = await crud.work_types.post(payload)
    response_object = await crud.work_types.get(work_type_id)
    return response_object

@router.get("/{id}/", response_model=WorkTypeDB)
async def read_work_type(id: int = Path(..., gt=0), user: User = Depends(get_current_user)):
    work_type_in_db = await crud.work_types.get(id)
    if not work_type_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work type not found")
    return work_type_in_db
