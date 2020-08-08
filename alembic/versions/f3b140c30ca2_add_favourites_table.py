"""add favourites table

Revision ID: f3b140c30ca2
Revises: 5efc0ba0a571
Create Date: 2020-08-08 19:50:10.317878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b140c30ca2'
down_revision = '5efc0ba0a571'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "favourites_users_asteroids",
        sa.Column("id_user", sa.BigInteger, sa.ForeignKey('users.id'), nullable=False),
        sa.Column("id_asteroid", sa.BigInteger, sa.ForeignKey('asteroids.id'), nullable=False),
    )


def downgrade():
    op.drop_table("favourites_users_asteroids")

