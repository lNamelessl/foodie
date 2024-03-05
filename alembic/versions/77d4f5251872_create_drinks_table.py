"""create drinks_table'

Revision ID: 77d4f5251872
Revises: 0158bf0da5ed
Create Date: 2023-11-04 08:07:10.679594

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "77d4f5251872"
down_revision: Union[str, None] = "0158bf0da5ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "drinks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("drinks", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("drinks")
