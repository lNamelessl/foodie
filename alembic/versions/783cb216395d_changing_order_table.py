"""changing order table

Revision ID: 783cb216395d
Revises: 39ee7b1dfd63
Create Date: 2023-11-12 10:48:09.821251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '783cb216395d'
down_revision: Union[str, None] = '39ee7b1dfd63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('orders',sa.Column('order_id',sa.Integer(),nullable=True),)
    pass


def downgrade() -> None:
    op.drop_column("order_id")
    pass
