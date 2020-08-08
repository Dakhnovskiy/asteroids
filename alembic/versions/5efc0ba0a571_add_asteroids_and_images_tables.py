"""add asteroids and images tables

Revision ID: 5efc0ba0a571
Revises: 05b4a2f6ea0d
Create Date: 2020-08-08 19:33:51.462186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5efc0ba0a571'
down_revision = '05b4a2f6ea0d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "asteroids",
        sa.Column("id", sa.BigInteger, primary_key=True, nullable=False),
    )

    op.create_table(
        "images",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column("path", sa.String(256), unique=True, nullable=False),
    )

    op.create_table(
        "asteroids_images",
        sa.Column("id_asteroid", sa.BigInteger, sa.ForeignKey('asteroids.id'), nullable=False),
        sa.Column("id_image", sa.BigInteger, sa.ForeignKey('images.id'), nullable=False),
    )


def downgrade():
    op.drop_table("asteroids_images")
    op.drop_table("images")
    op.drop_table("asteroids")
