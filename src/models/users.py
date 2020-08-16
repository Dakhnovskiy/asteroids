import sqlalchemy as sa

from src.app.db import metadata


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
