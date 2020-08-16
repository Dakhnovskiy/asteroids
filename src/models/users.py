from typing import List

import sqlalchemy as sa

from src.app.db import metadata, db


users = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('login', sa.String(256), unique=True, nullable=False),
    sa.Column('password_hash', sa.String(256), nullable=False),
)


favourites_users_asteroids = sa.Table(
    'favourites_users_asteroids',
    metadata,
    sa.Column('user_id', sa.BigInteger, sa.ForeignKey('users.id'), nullable=False),
    sa.Column('asteroid_name', sa.String(256), nullable=False),
)


class User:
    @classmethod
    async def get_by_login(cls, login: str) -> dict:
        query = users.select().where(users.c.login == login)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def get_by_id(cls, user_id: int) -> dict:
        query = users.select().where(users.c.id == user_id)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def create(cls, login: str, password_hash: str) -> int:
        query = users.insert().values(login=login, password_hash=password_hash)
        user_id = await db.execute(query)
        return user_id


class UserFavourites:
    @classmethod
    async def get_by_user_id(cls, user_id: int) -> List[str]:
        query = favourites_users_asteroids.select().\
            where(favourites_users_asteroids.c.user_id == user_id).\
            with_only_columns(columns=[favourites_users_asteroids.c.asteroid_name])
        favourites_asteroids = await db.fetch_all(query)
        return [favourites_asteroid[0] for favourites_asteroid in favourites_asteroids]

    @classmethod
    async def create(cls, user_id: int, asteroid_name: str) -> None:
        query = favourites_users_asteroids.insert().values(user_id=user_id, asteroid_name=asteroid_name)
        await db.execute(query)
