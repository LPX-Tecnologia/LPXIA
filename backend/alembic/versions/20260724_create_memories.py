"""create memories table

Revision ID: 20260724_create_memories
Revises: 20260724_create_users
Create Date: 2026-07-24 00:01:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = "20260724_create_memories"
down_revision = "20260724_create_users"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "memories",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("memory_type", sa.String(), nullable=False, server_default="fact"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_memories_id"), "memories", ["id"], unique=False)
    op.create_index(op.f("ix_memories_user_id"), "memories", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_memories_user_id"), table_name="memories")
    op.drop_index(op.f("ix_memories_id"), table_name="memories")
    op.drop_table("memories")
