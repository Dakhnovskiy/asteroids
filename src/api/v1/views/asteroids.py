from fastapi import APIRouter, Query
from starlette.requests import Request

from src.api.v1.views.serializers import Asteroids
from src.asteroids_data.asteroids_data import get_asteroid_data_from_storage_by_name
from src.images.images import get_images_ids_by_asteroid_name, get_image_download_url

asteroids_views = APIRouter()


@asteroids_views.get('/asteroids', response_model=Asteroids, status_code=200)
async def get_asteroid(request: Request, name: str = Query(..., min_length=1)):
    asteroid_data = await get_asteroid_data_from_storage_by_name(name)
    images_ids = await get_images_ids_by_asteroid_name(name)
    asteroid_data['images_links'] = [get_image_download_url(str(request.base_url), image_id) for image_id in images_ids]
    return asteroid_data
