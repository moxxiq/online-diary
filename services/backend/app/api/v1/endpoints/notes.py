from fastapi import APIRouter, HTTPException, status,  Path

import app.core.crud as crud
from app.core.schemas.notes import NoteDB, NoteSchema

router = APIRouter()


@router.post("/", response_model=NoteDB, status_code=status.HTTP_201_CREATED)
async def create_note(payload: NoteSchema):
    note_id = await crud.notes.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

@router.get("/{id}/", response_model=NoteDB)
async def read_note(id: int = Path(..., gt=0),):
    note = await crud.notes.get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


@router.get("/", response_model=list[NoteDB])
async def read_all_notes():
    return await crud.notes.get_all()

@router.put("/{id}/", response_model=NoteDB)
async def update_note(payload: NoteSchema, id: int = Path(..., gt=0),):
    note = await crud.notes.get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    note_id = await crud.notes.put(id, payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int = Path(..., gt=0)):
    note = await crud.notes.get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    await crud.notes.delete(id)

    return note

