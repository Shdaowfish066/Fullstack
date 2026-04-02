"""add user role for admin panel

Revision ID: 2f4c8a9d11ab
Revises: 11b3c7d9e2f4
Create Date: 2026-04-02 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2f4c8a9d11ab"
down_revision: Union[str, Sequence[str], None] = "11b3c7d9e2f4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("role", sa.String(length=32), nullable=True, server_default="user"))
    op.create_index(op.f("ix_users_role"), "users", ["role"], unique=False)
    op.execute("UPDATE users SET role = 'user' WHERE role IS NULL")
    op.alter_column("users", "role", nullable=False, server_default="user")


def downgrade() -> None:
    op.drop_index(op.f("ix_users_role"), table_name="users")
    op.drop_column("users", "role")