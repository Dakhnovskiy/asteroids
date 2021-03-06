import datetime
from typing import List

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from fastapi.responses import FileResponse

from src.api.v1.views.serializers import Images
from src.asteroids_data.asteroids_data import exists_asteroids_data_by_names
from src.images.images import save_image, get_image_data_by_id

images_views = APIRouter()


@images_views.post('/images', response_model=Images, status_code=201)
async def upload_image(
        file: UploadFile = File(..., alias='file'),
        image_datetime: datetime.datetime = Form(...),
        asteroids_names: List[str] = Form(...),
):
    exists_asteroids = await exists_asteroids_data_by_names(asteroids_names)
    if not exists_asteroids:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'Incorrect asteroids names')

    image = await save_image(await file.read(), file.filename, image_datetime, asteroids_names)
    return image


@images_views.get('/images/{image_id}', response_model=Images, status_code=200)
async def get_image(image_id: int):
    image = await get_image_data_by_id(image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'image id {image_id} not found')
    return image


@images_views.get('/images/{image_id}/file')
async def get_image_file(image_id: int):
    image = await get_image_data_by_id(image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'image id {image_id} not found')
    return FileResponse(image['path'])
