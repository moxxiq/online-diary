from datetime import date

import pytest

import app.core.crud as crud
from app.core.authorization import get_password_hash, create_access_token
from app.core.schemas.users import UserInDB, NewUser

# Declare DB users
fictive_users = dict(
    keys=["email", "type"],
    values=[
        ['admin@kpi.ua', 1],
        ['teacher.or.someone.else@kpi.ua', 2],
        ['evil.hacker@kpi.ua', 1],
    ]
)
fictive_db_users = [dict(zip(fictive_users["keys"], w)) for w in fictive_users["values"]]


def gen_db_users(id=1, email='sample@email.com', hashed_password="password", type=1,
                 name='admin', surname='admin', birthday=date(2000, 1, 1), ):
    return UserInDB(
        id=id, email=email, hashed_password=get_password_hash(hashed_password), type=type,
        name=name, surname=surname, birthday=birthday,
    )


async def get_by_email(email: str):
    for u in fictive_db_users:
        if u["email"] == email:
            return gen_db_users(**u)
    return None


@pytest.mark.parametrize(
    "email, status_code",
    [
        ['admin@kpi.ua', 201],  # Normal case
        ['teacher.or.someone.else@kpi.ua', 403],  # User has no privileges
    ],
)
def test_create_user(test_app, monkeypatch, email, status_code):
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
            headers={'Authorization': f'Bearer {user_AT}'}, )
    except Exception as e:
        print(e)
        assert e == ''
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email, status_code",
    [
        ['evil.hacker@kpi.ua', 200],  # Normal case
        ['another.hacker@kpi.ua', 401],  # User has credentials but his not in database
    ],
)
def test_read_users_me(test_app, monkeypatch, email, status_code):
    monkeypatch.setattr(crud.users, "get_by_email", get_by_email)

    user_AT = create_access_token(data={"sub": email})
    response = test_app.get(
        "/users/me/",
        headers={'Authorization': f'Bearer {user_AT}'}, )
    assert response.status_code == status_code


def test_read_users_me_unauthorized(test_app):
    response = test_app.get(
        "/users/me/",
    )
    assert response.status_code == 401
