"""create tables

Revision ID: 124c5bebe751
Revises: 9b99b2434ae5
Create Date: 2024-05-10 04:37:30.079590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '124c5bebe751'
down_revision: Union[str, None] = '9b99b2434ae5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
