"""add unique constarint to favourites

Revision ID: 197f642ee4c2
Revises: bfce0272de5b
Create Date: 2020-08-16 23:10:51.662845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '197f642ee4c2'
down_revision = 'bfce0272de5b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(
        'uq_favourites_users_asteroids', 'favourites_users_asteroids', ['user_id', 'asteroid_name']
    )


def downgrade():
    op.drop_constraint('uq_favourites_users_asteroids')
