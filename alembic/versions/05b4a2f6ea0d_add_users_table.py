"""add users table

Revision ID: 05b4a2f6ea0d
Revises: 
Create Date: 2020-08-08 18:42:03.258280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05b4a2f6ea0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column("login", sa.String(256), unique=True, nullable=False),
        sa.Column("password", sa.String(256), nullable=False),
    )


def downgrade():
    op.drop_table("users")
