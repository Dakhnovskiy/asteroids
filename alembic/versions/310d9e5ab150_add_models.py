"""add models

Revision ID: 310d9e5ab150
Revises: 
Create Date: 2020-08-16 11:36:47.233511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310d9e5ab150'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('login', sa.String(256), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(256), nullable=False),
    )

    op.create_table(
        'favourites_users_asteroids',
        sa.Column('user_id', sa.BigInteger, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('asteroid_name', sa.String(256), nullable=False),
    )

    op.create_table(
        'images',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('image_datetime', sa.DateTime, nullable=True),
        sa.Column('path', sa.String(256), unique=True, nullable=False),
    )

    op.create_table(
        'asteroids_images',
        sa.Column('asteroid_name', sa.String(256), nullable=False),
        sa.Column('image_id', sa.BigInteger, sa.ForeignKey('images.id'), nullable=False),
    )


def downgrade():
    op.drop_table('asteroids_images')
    op.drop_table('images')
    op.drop_table('favourites_users_asteroids')
    op.drop_table('users')
