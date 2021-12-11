from fastapi import APIRouter, status, HTTPException, Path, Depends

import app.core.crud as crud
from app.core.authorization import get_current_user, get_current_user_with_scopes
from app.core.schemas.users import UserInDB
from app.core.schemas.subjects import Subject, SubjectDB

router = APIRouter()



@router.post("/", response_model=SubjectDB, status_code=status.HTTP_201_CREATED)
async def create_subject(payload: Subject, current_user: UserInDB = Depends(get_current_user_with_scopes([1, 2]))):
    subject_in_db = await crud.subjects.get_by_attrs(payload)
    if subject_in_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This subject is already exists")
    subject_id = await crud.subjects.post(payload)
    response_object = await crud.subjects.get(subject_id)
    return response_object

@router.get("/{id}/", response_model=SubjectDB)
async def read_subject(id: int = Path(..., gt=0), user: UserInDB = Depends(get_current_user)):
    subject_in_db = await crud.subjects.get(id)
    if not subject_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")
    return subject_in_db
