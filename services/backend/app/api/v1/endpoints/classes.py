from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import User
from app.core.schemas.classes import Class, ClassDB

router = APIRouter()



@router.post("/", response_model=ClassDB, status_code=status.HTTP_201_CREATED)
async def create_class(payload: Class, current_user: User = Depends(get_current_user_with_scopes([1, 2]))):
    class_in_db = await crud.classes.get_by_attrs(payload)
    if class_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This class is already exists")
    class_id = await crud.classes.post(payload)
    response_object = await crud.classes.get(class_id)
    return response_object

@router.get("/{id}/", response_model=ClassDB)
async def read_class(id: int = Path(..., gt=0),):
    class_in_db = await crud.classes.get(id)
    if not class_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return class_in_db