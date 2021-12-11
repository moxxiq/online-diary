from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserInDB
from app.core.schemas.works import Work, WorkDB, WorkContent

router = APIRouter()

@router.post("/", response_model=WorkDB, status_code=status.HTTP_201_CREATED)
async def create_work(payload: Work, current_user: UserInDB = Depends(get_current_user_with_scopes([1, 2]))):
    work_id = await crud.works.post(payload)
    response_object = await crud.works.get(work_id)
    return response_object

@router.put("/{id}/", response_model=WorkContent)
async def update_work(payload: WorkContent, id: int = Path(..., gt=0), current_user: UserInDB = Depends(get_current_user_with_scopes([1, 2]))):
    work = await crud.works.get(id)
    if not work:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found")

    work_id = await crud.works.put(id, payload)

    response_object = {
        "id": work_id,
        "headline": payload.headline,
        "deadline": payload.deadline,
        "description": payload.description,
        "work_type_id": payload.work_type_id,
    }
    return response_object

@router.get("/{id}/", response_model=WorkDB)
async def read_work(id: int = Path(..., gt=0), current_user: UserInDB = Depends(get_current_user_with_scopes([1, 2, 3]))):
    work_in_db = await crud.works.get(id)
    if not work_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found")
    return work_in_db

@router.delete("/{id}/", response_model=WorkDB)
async def delete_work(id: int = Path(..., gt=0), current_user: UserInDB = Depends(get_current_user_with_scopes([1, 2]))):
    work_in_db = await crud.works.get(id)
    if not work_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found")
    await crud.works.delete((id))
    return work_in_db

# TODO: add gett all work with the same teacher subject class
# i. e. like: /workplaces/{id}/works/
