"""create account table

Revision ID: 538a05c8157d
Revises: 87dadc767090
Create Date: 2024-05-20 15:40:29.425954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '538a05c8157d'
down_revision: Union[str, None] = '87dadc767090'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
