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
    async def get(cls, image_id):
        query = images.select().where(images.c.id == image_id)
        image = await db.fetch_one(query)
        return image

    @classmethod
    async def create(cls, image_path, image_datetime):
        query = images.insert().values(path=image_path, image_datetime=image_datetime)
        image_id = await db.execute(query)
        return image_id
