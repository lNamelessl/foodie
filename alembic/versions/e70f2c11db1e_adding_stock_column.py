"""adding stock column

Revision ID: e70f2c11db1e
Revises: 99965f3d87e2
Create Date: 2023-11-28 16:50:12.596127

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e70f2c11db1e"
down_revision: Union[str, None] = "99965f3d87e2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("orders", sa.Column("Stock_Quantity", sa.Integer, nullable=True))
    


def downgrade() -> None:
    op.drop_column("orders", "Stock_Quantity")
    
