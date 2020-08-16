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
    async def create(cls, login: str, password_hash: str) -> int:
        query = users.insert().values(login=login, password_hash=password_hash)
        user_id = await db.execute(query)
        return user_id
