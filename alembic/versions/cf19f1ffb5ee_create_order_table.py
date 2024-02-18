"""create order_table

Revision ID: cf19f1ffb5ee
Revises: c6eb8202cb03
Create Date: 2023-11-11 10:54:44.407019

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cf19f1ffb5ee"
down_revision: Union[str, None] = "c6eb8202cb03"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("food", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
    )
    # sa.ForeignKeyConstraint('orders_users_fk',source_table="orders",referent_table="users"),
    # refcolumns="columns=ousers,orders" ,local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    


def downgrade() -> None:
    # op.drop_constraint('orders_users_fk',table_name='orders')
    op.drop_table("orders")
    
