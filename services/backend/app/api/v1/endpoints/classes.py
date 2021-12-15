from typing import Optional

from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.classes import Class, ClassDB
from app.core.schemas.users import UserWithID

router = APIRouter()


@router.post("/", response_model=ClassDB, status_code=status.HTTP_201_CREATED)
async def create_class(payload: Class, current_user: UserWithID = Depends(get_current_user_with_scopes([1, 2]))):
    class_in_db = await crud.classes.get_by_attrs(payload)
    if class_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This class is already exists")
    class_id = await crud.classes.post(payload)
    response_object = await crud.classes.get(class_id)
    return response_object


@router.get("/{id}/", response_model=ClassDB)
async def read_class(id: int = Path(..., gt=0), user: UserWithID = Depends(get_current_user)):
    class_in_db = await crud.classes.get(id)
    if not class_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")
    return class_in_db


@router.get("/", response_model=list[ClassDB])
async def search_classes(class_number: Optional[int], class_name: Optional[str] = "", user: UserWithID = Depends(get_current_user)):
    return await crud.classes.search_class(class_number, class_name)
