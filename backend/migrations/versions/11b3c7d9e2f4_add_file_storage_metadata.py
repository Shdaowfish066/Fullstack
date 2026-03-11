"""add file storage metadata

Revision ID: 11b3c7d9e2f4
Revises: 10a36f762b2d, b2c3d4e5f6a7, refresh_token_table
Create Date: 2026-03-11 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "11b3c7d9e2f4"
down_revision: Union[str, Sequence[str], None] = ("10a36f762b2d", "b2c3d4e5f6a7", "refresh_token_table")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("files", sa.Column("file_url", sa.String(length=1000), nullable=True))
    op.add_column("files", sa.Column("storage_provider", sa.String(length=32), nullable=True, server_default="local"))
    op.add_column("files", sa.Column("storage_asset_id", sa.String(length=255), nullable=True))
    op.create_index(op.f("ix_files_storage_asset_id"), "files", ["storage_asset_id"], unique=False)

    op.execute("UPDATE files SET file_url = file_path WHERE file_url IS NULL")
    op.execute("UPDATE files SET storage_provider = 'local' WHERE storage_provider IS NULL")

    op.alter_column("files", "file_url", nullable=False)
    op.alter_column("files", "storage_provider", nullable=False, server_default="local")


def downgrade() -> None:
    op.drop_index(op.f("ix_files_storage_asset_id"), table_name="files")
    op.drop_column("files", "storage_asset_id")
    op.drop_column("files", "storage_provider")
    op.drop_column("files", "file_url")