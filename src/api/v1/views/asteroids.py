from fastapi import APIRouter, Query

from src.api.v1.views.serializers import Asteroids
from src.asteroids_data.asteroids_data import get_asteroid_data_from_storage_by_name

asteroids_views = APIRouter()


@asteroids_views.get('/asteroids', response_model=Asteroids, status_code=200)
async def get_asteroid(name: str = Query(..., min_length=1)):
    asteroid_data = await get_asteroid_data_from_storage_by_name(name)
    return asteroid_data
