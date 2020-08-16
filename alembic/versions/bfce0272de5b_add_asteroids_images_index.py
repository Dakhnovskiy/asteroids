"""add asteroids images index

Revision ID: bfce0272de5b
Revises: 310d9e5ab150
Create Date: 2020-08-16 21:45:45.803062

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'bfce0272de5b'
down_revision = '310d9e5ab150'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('idx_asteroid_name', 'asteroids_images', ['asteroid_name'])


def downgrade():
    op.drop_index('idx_asteroid_name')
