"""create account table

Revision ID: e0f94e9a45b8
Revises: 124c5bebe751
Create Date: 2024-05-15 20:30:45.780528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0f94e9a45b8'
down_revision: Union[str, None] = '124c5bebe751'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
