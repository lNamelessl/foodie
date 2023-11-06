"""create main_meal table'

Revision ID: adecfeff53b3
Revises: af559278db60
Create Date: 2023-11-04 07:17:07.453365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adecfeff53b3'
down_revision: Union[str, None] = 'af559278db60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('main_dish',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('main_dish',sa.String(),nullable=False),
                    sa.Column('price',sa.Integer(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('main_dish')
    pass
