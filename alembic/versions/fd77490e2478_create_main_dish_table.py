"""create main_dish table'

Revision ID: fd77490e2478
Revises: adecfeff53b3
Create Date: 2023-11-04 07:44:40.333327

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fd77490e2478"
down_revision: Union[str, None] = "adecfeff53b3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
