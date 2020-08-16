import datetime
from typing import List

import sqlalchemy as sa

from src.app.db import metadata, db

images = sa.Table(
    'images',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('image_datetime', sa.DateTime, nullable=True),
    sa.Column('path', sa.String(256), unique=True, nullable=False),
)


asteroids_images = sa.Table(
    'asteroids_images',
    metadata,
    sa.Column('asteroid_name', sa.String(256), nullable=False),
    sa.Column('image_id', sa.BigInteger, sa.ForeignKey('images.id'), nullable=False),
)


class Image:
    @classmethod
    async def get(cls, image_id: int) -> dict:
        query = images.select().where(images.c.id == image_id)
        image = await db.fetch_one(query)
        return image

    @classmethod
    async def create(cls, image_path: str, image_datetime: datetime.datetime) -> int:
        query = images.insert().values(path=image_path, image_datetime=image_datetime)
        image_id = await db.execute(query)
        return image_id


class AsteroidImage:
    @classmethod
    async def get_images_list_by_asteroid_name(cls, asteroid_name):
        query = asteroids_images.select().where(asteroids_images.c.asteroid_name == asteroid_name)
        images_ids = await db.fetch_val(query, column=asteroids_images.c.image_id)
        return images_ids

    @classmethod
    async def create_list(cls, image_id: int, asteroid_names: List[str]):
        query = asteroids_images.insert().values(
            [{'image_id': image_id, 'asteroid_name': asteroid_name} for asteroid_name in asteroid_names]
        )
        await db.execute(query)
