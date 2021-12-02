import json
from datetime import date

import pytest

import app.core.crud as crud
from app.core.authorization import get_password_hash, create_access_token
from app.core.schemas.users import UserInDB, NewUser


@pytest.mark.parametrize(
    "email, status_code",
    [
        ['evil.hacker@kpi.ua', 200],  # Normal case
        ['another.hacker@kpi.ua', 401], # User has credentials but his not in database
    ],
)
def test_read_users_me(test_app, monkeypatch, email, status_code):
    user_email = 'evil.hacker@kpi.ua'
    user_in_db = UserInDB(
        id=1,
        email=user_email,
        hashed_password=get_password_hash("password"),
        type=1,
        name='admin',
        surname='admin',
        midname='anything',
        birthday=date(2000, 1, 1),
    )
    async def get_by_email(email):
        if email == user_email:
            return user_in_db
        return None
    monkeypatch.setattr(crud.users, "get_by_email", get_by_email)

    user_AT = create_access_token(data={"sub": email})
    response = test_app.get(
        "/users/me/",
        headers={'Authorization': f'Bearer {user_AT}'},)
    assert response.status_code == status_code

def test_read_users_me_unauthorized(test_app):
    response = test_app.get(
        "/users/me/",
    )
    assert response.status_code == 401

@pytest.mark.parametrize(
    "email, status_code",
    [
        ['admin@kpi.ua', 201],  # Normal case
        ['teacher.or.someone.else@kpi.ua', 403], # User has credentials but his not in database
    ],
)
def test_create_user(test_app, monkeypatch, email, status_code):
    user_in_db = lambda email, type: UserInDB(
        id=1,
        email=email,
        hashed_password=get_password_hash("password"),
        type=type,
        name='admin',
        surname='admin',
        birthday=date(2000, 1, 1),
    )
    async def get_by_email(email):
        if email == 'admin@kpi.ua':
            return user_in_db(email, 1)
        if email == 'teacher.or.someone.else@kpi.ua':
            return user_in_db(email, 2)
        return None

    async def nothing(*args, **kwargs):
        return None

    monkeypatch.setattr(crud.users, "get_by_email", get_by_email)
    monkeypatch.setattr(crud.users, "get", nothing)
    monkeypatch.setattr(crud.users, "post", nothing)

    user_AT = create_access_token(data={"sub": email})
    try:
        response = test_app.post(
            "/users/",
            data=NewUser(name='New', surname='User', birthday=date(2000, 1, 1), password='qwe',
                         email='em@i.l', type=2).json(),
            headers={'Authorization': f'Bearer {user_AT}'},)
    except Exception as e:
        print(e)
        assert e == ''
    assert response.status_code == status_code
