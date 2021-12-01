import pytest
import json

from fastapi.security import OAuth2PasswordRequestForm

from app.api.v1.endpoints.authorization import login_for_access_token
from app.core import crud
from app.core.authorization import get_password_hash
from app.core.schemas.users import UserInDB

# @pytest.mark.parametrize(
#     "email, password, status_code",
#     [
#         ["evil.hacker@kpi.ua", "easy-password", 200],
#         ["teacher.without.account@kpi.ua", "password", 401],
#     ],
# )
# def test_login_for_access_token(test_app, monkeypatch, email, password, status_code):
#     async def get_by_email(email):
#         if email == 'evil.hacker@kpi.ua':
#             return UserInDB(email=email, hashed_password=get_password_hash("easy-password"))
#         return None
#     monkeypatch.setattr(crud.users, "get_by_email", get_by_email)
#
#     response = test_app.post(f"/token", data=json.dumps(dict(username=email, password=password)),)
#     assert response.status_code == status_code