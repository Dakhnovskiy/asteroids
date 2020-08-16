from fastapi import APIRouter, status, HTTPException

from src.api.v1.views.serializers import UserInfo, UserCreate
from src.users_data.users_data import get_user_by_login, create_user_data

users_views = APIRouter()


@users_views.post('/users', response_model=UserInfo, status_code=201)
async def create_user(
        user: UserCreate
):
    user_data = await get_user_by_login(user.login)
    if user_data:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'{user.login} already registered')

    user_id = await create_user_data(user.login, user.password)

    return {
        'id': user_id,
        'login': user.login,
    }
