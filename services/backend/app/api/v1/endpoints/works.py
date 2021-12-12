from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserWithID
from app.core.schemas.works import Work, WorkDB, WorkContent

router = APIRouter()

@router.post("/works/", response_model=WorkDB, status_code=status.HTTP_201_CREATED)
async def create_work(payload: Work, current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    # TODO: Fix vulnerability so anoter teacher couldn't create task for another groups
    work_id = await crud.works.post(payload)
    response_object = await crud.works.get(work_id)
    return response_object

@router.put("/works/{id}/", response_model=WorkContent)
async def update_work(payload: WorkContent, id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
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

@router.get("/works/{id}/", response_model=WorkDB)
async def read_work(id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    work_in_db = await crud.works.get(id)
    if not work_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found")
    return work_in_db

@router.delete("/works/{id}/", response_model=WorkDB)
async def delete_work(id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    work_in_db = await crud.works.get(id)
    if not work_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found")
    await crud.works.delete((id))
    return work_in_db

@router.get("/workplaces/{workplace_id}/works/", response_model=list[WorkDB])
async def get_all_workplace_works(workplace_id: int = Path(..., gt=0), current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2, 3]))):
    workplace_in_db = await crud.workplaces.get(workplace_id)
    if not workplace_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workplace not found")
    if current_user.get("type") not in [1, 2]: # Teacher -> can view all
        if not await crud.classes.if_student_in_class(student_id=current_user.get(id),
                                                      class_id=workplace_in_db.class_id):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Student is not in workplaces class")
    return await crud.works.get_all_workplace_works(workplace_id)
