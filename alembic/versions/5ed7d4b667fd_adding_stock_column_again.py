"""adding stock column again

Revision ID: 5ed7d4b667fd
Revises: e70f2c11db1e
Create Date: 2023-11-28 16:55:52.678046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ed7d4b667fd'
down_revision: Union[str, None] = 'e70f2c11db1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('orders','Stock_Quantity')
    op.add_column('main_dish',sa.Column('Stock_Quantity',sa.Integer,nullable=True))
    op.add_column('side_dish',sa.Column('Stock_Quantity',sa.Integer,nullable=True))
    op.add_column('drinks',sa.Column('Stock_Quantity',sa.Integer,nullable=True))
    op.add_column('desert',sa.Column('Stock_Quantity',sa.Integer,nullable=True))
    pass


def downgrade() -> None:
    op.add_column('orders',sa.Column('Stock_Quantity',sa.Integer,nullable=True))
    op.drop_column('main_dish','Stock_Quantity')
    op.drop_column('side_dish','Stock_Quantity')
    op.drop_column('drinks','Stock_Quantity')
    op.drop_column('desert','Stock_Quantity')
    pass
