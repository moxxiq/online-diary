from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from app.config import FRONTEND_PATH

router = APIRouter()

@router.get("/")
async def redirected():
    url = FRONTEND_PATH
    print(f"{url = }")
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    response = RedirectResponse(url=FRONTEND_PATH)
    return response
