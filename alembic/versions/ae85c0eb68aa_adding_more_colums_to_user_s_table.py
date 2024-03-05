"""adding more colums to user's table

Revision ID: ae85c0eb68aa
Revises: 783cb216395d
Create Date: 2023-11-13 17:18:33.954920

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ae85c0eb68aa"
down_revision: Union[str, None] = "783cb216395d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("full_name", sa.String(), nullable=False))
    op.add_column("users", sa.Column("Address", sa.String(), nullable=False))



def downgrade() -> None:
    op.drop_column("users", "full_name")
    op.drop_column("users", "Address")
