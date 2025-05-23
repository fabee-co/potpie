"""Adding support for projects

Revision ID: 20240812190934_5ceb460ac3ef
Revises: 20240812184546_6d16b920a3ec
Create Date: 2024-08-12 19:09:34.063355

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "20240812190934_5ceb460ac3ef"
down_revision: Union[str, None] = "20240812184546_6d16b920a3ec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("directory", sa.Text(), nullable=True),
        sa.Column("is_default", sa.Boolean(), nullable=True),
        sa.Column("project_name", sa.Text(), nullable=True),
        sa.Column("properties", postgresql.BYTEA(), nullable=True),
        sa.Column("repo_name", sa.Text(), nullable=True),
        sa.Column("branch_name", sa.Text(), nullable=True),
        sa.Column("user_id", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("commit_id", sa.String(length=255), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.CheckConstraint(
            "status IN ('created', 'ready', 'error')", name="check_status"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.uid"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("directory"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("projects")
    # ### end Alembic commands ###
