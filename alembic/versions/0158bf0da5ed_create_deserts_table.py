"""create deserts_table'

Revision ID: 0158bf0da5ed
Revises: 1cf4dd621a0d
Create Date: 2023-11-04 08:01:55.189233

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0158bf0da5ed"
down_revision: Union[str, None] = "1cf4dd621a0d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "desert",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("desert", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("desert")
