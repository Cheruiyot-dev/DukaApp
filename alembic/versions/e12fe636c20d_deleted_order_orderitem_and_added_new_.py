"""deleted order, orderItem and added new fields in Sale table

Revision ID: e12fe636c20d
Revises: 2a242f8a7ce1
Create Date: 2024-05-19 21:42:51.224318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e12fe636c20d'
down_revision: Union[str, None] = '2a242f8a7ce1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
