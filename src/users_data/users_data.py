from typing import List

from src.hash.hash import get_hash
from src.models.users import User, UserFavourites


async def get_user_by_login(login: str) -> dict:
    """
    get user data by login
    :param login: user login
    :return: user data
    """
    return await User.get_by_login(login)


async def get_user_by_id(user_id: int) -> dict:
    """
    get user data by id
    :param user_id: user id
    :return: user data
    """
    return await User.get_by_id(user_id)


async def create_user_data(login: str, password: str) -> int:
    """
    create user
    :param login: user login
    :param password: user password
    """

    return await User.create(login, password_hash=get_hash(password))


async def create_user_favourites(user_id: int, asteroid_name: str) -> None:
    """
    add asteroid name to users favourites
    :param user_id: user id
    :param asteroid_name: asteroid name
    """

    await UserFavourites.create(user_id, asteroid_name)


async def get_user_favourites(user_id: int) -> List[str]:
    """
    get users favourites asteroids names
    :param user_id: user id
    """

    return await UserFavourites.get_by_user_id(user_id)
