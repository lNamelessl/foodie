"""create side_dish_table'

Revision ID: 1cf4dd621a0d
Revises: fd77490e2478
Create Date: 2023-11-04 07:51:00.975838

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1cf4dd621a0d"
down_revision: Union[str, None] = "fd77490e2478"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "side_dish",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("side_dish", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("side_dish")
