"""adding fkeys_table

Revision ID: 39ee7b1dfd63
Revises: cf19f1ffb5ee
Create Date: 2023-11-11 11:44:07.918613

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "39ee7b1dfd63"
down_revision: Union[str, None] = "cf19f1ffb5ee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        "order_users_fk",
        source_table="orders",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    


def downgrade() -> None:
    op.drop_constraint("orders_users_fk", table_name="orders")
    
