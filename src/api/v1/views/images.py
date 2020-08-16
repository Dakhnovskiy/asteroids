import datetime
from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from src.asteroids_data.asteroids_data import exists_asteroids_data_by_names
from src.images.images import save_image

images_views = APIRouter()


@images_views.post('/images', status_code=201)
async def upload_image(
        file: UploadFile = File(..., alias='file'),
        image_datetime: datetime.datetime = Form(...),
        asteroids_names: List[str] = Form(...),
):
    exists_asteroids = await exists_asteroids_data_by_names(asteroids_names)
    if exists_asteroids:
        image = await save_image(await file.read(), file.filename, image_datetime, asteroids_names)

        return {"message": image}
    else:
        return {"message": "assssssss"}
