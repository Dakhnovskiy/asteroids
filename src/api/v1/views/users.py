from fastapi import APIRouter, status, HTTPException

from src.api.v1.views.serializers import UserInfo, UserCreate, UserFavourites, UserFavouritesInfo
from src.asteroids_data.asteroids_data import exists_asteroid_data_by_name
from src.users_data.users_data import get_user_by_login, create_user_data, get_user_by_id, create_user_favourites, \
    get_user_favourites

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


@users_views.post('/users/{user_id}/favourites', status_code=204)
async def create_favourites(
        user_id: int,
        user_favourites: UserFavourites
):
    user_data = await get_user_by_id(user_id)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user id {user_id} not found'
        )

    asteroid_exists = await exists_asteroid_data_by_name(user_favourites.asteroid_name)
    if not asteroid_exists:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'asteroid name {user_favourites.asteroid_name} not found'
        )

    await create_user_favourites(user_id, user_favourites.asteroid_name)


@users_views.get('/users/{user_id}/favourites', response_model=UserFavouritesInfo, status_code=200)
async def get_favourites(
        user_id: int,
):
    user_data = await get_user_by_id(user_id)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user id {user_id} not found'
        )

    user_favourites = await get_user_favourites(user_id)

    return {
        'user_id': user_id,
        'favourites': user_favourites
    }
