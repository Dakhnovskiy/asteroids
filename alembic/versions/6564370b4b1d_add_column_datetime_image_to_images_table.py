"""add column datetime_image to images table

Revision ID: 6564370b4b1d
Revises: f3b140c30ca2
Create Date: 2020-08-08 19:55:48.308091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6564370b4b1d'
down_revision = 'f3b140c30ca2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('images', sa.Column('datetime_image', sa.DateTime, nullable=True))


def downgrade():
    op.drop_column('images', 'datetime_image')
