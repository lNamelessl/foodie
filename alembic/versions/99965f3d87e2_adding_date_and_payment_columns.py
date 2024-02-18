"""adding date and payment columns

Revision ID: 99965f3d87e2
Revises: ae85c0eb68aa
Create Date: 2023-11-23 10:35:09.459009

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "99965f3d87e2"
down_revision: Union[str, None] = "ae85c0eb68aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "orders",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("NOW()"),
            nullable=False,
        ),
    )
    op.add_column(
        "orders",
        sa.Column("payment", sa.Boolean(), server_default="FALSE", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("orders")
    op.drop_column("orders")
