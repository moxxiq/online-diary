from datetime import datetime, timedelta

from app.config import SECRET_KEY, ALGORITHM
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

import app.core.crud as crud
from app.core.schemas.users import User
from app.core.schemas.authorization import TokenData

ACCESS_TOKEN_EXPIRE_MINUTES = 10080 # or 30 with refresh token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password) -> str:
    return pwd_context.hash(password)

async def authenticate_user(email: str, password: str):
    user = await crud.users.get_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.get("hashed_password")):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await crud.users.get_by_email(token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_user_with_scopes(scopes: list[int]):
    """
    Decorator сlosure to check if user have sufficient privileges
    :param scopes: List of obligatory privileges
    :return: Dependency function to get user with sufficient privileges
    TODO: document exceptions https://fastapi.tiangolo.com/tutorial/metadata/
        https://fastapi.tiangolo.com/tutorial/handling-errors/
    """
    rights_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Insufficient rights to a resource",
    )
    async def get_concrete_user(current_user: User = Depends(get_current_user)):
        if current_user.get("type") in scopes:
            return current_user
        raise rights_exception
    return get_concrete_user