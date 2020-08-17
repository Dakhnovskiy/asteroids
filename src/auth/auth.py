from datetime import timedelta, datetime
from typing import Optional

from jose import jwt

from src.app.config import config
from src.hash.hash import get_hash
from src.users_data.users_data import get_user_by_login


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    verify password
    :param plain_password: password
    :param hashed_password: hashed password
    :return: check result
    """
    return get_hash(plain_password) == hashed_password


async def authenticate_user(login: str, password: str) -> bool:
    """
    check user login/password
    :param login: user login
    :param password: user password
    :return: check result
    """
    user = await get_user_by_login(login)
    if not user:
        return False
    if not verify_password(password, user['password_hash']):
        return False
    return True


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    create access token
    :param data: data to encode
    :param expires_delta: token expire time
    :return: token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt
