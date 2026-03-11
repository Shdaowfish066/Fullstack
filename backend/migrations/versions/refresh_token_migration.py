"""add refresh token table

Revision ID: refresh_token_table
Revises: 
Create Date: 2026-03-10 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'refresh_token_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if 'refresh_tokens' not in inspector.get_table_names():
        op.create_table('refresh_tokens',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('token', sa.String(length=512), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )

    existing_indexes = {index['name'] for index in inspector.get_indexes('refresh_tokens')}
    token_index = op.f('ix_refresh_tokens_token')
    user_index = op.f('ix_refresh_tokens_user_id')

    if token_index not in existing_indexes:
        op.create_index(token_index, 'refresh_tokens', ['token'], unique=True)
    if user_index not in existing_indexes:
        op.create_index(user_index, 'refresh_tokens', ['user_id'], unique=False)


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if 'refresh_tokens' not in inspector.get_table_names():
        return

    existing_indexes = {index['name'] for index in inspector.get_indexes('refresh_tokens')}
    token_index = op.f('ix_refresh_tokens_token')
    user_index = op.f('ix_refresh_tokens_user_id')

    if user_index in existing_indexes:
        op.drop_index(user_index, table_name='refresh_tokens')
    if token_index in existing_indexes:
        op.drop_index(token_index, table_name='refresh_tokens')
    op.drop_table('refresh_tokens')
