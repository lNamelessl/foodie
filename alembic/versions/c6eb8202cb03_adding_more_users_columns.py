"""adding more users columns

Revision ID: c6eb8202cb03
Revises: 0d93b6d803cd
Create Date: 2023-11-08 13:07:52.828948

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c6eb8202cb03"
down_revision: Union[str, None] = "0d93b6d803cd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("order", sa.String(), nullable=True),
    )
    


def downgrade() -> None:
    op.drop_column("order")
    op.drop_column("phone_number")
    
