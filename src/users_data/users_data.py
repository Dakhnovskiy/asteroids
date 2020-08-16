from src.hash.hash import get_hash
from src.models.users import User


async def get_user_by_login(login: str) -> dict:
    """
    get user data by login
    :param login: user login
    :return: user data
    """
    return await User.get_by_login(login)


async def create_user_data(login: str, password: str) -> int:
    """
    create user
    :param login: user login
    :param password: user password
    """

    return await User.create(login, password_hash=get_hash(password))
