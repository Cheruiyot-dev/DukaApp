"""delete all product

Revision ID: 2a242f8a7ce1
Revises: e0f94e9a45b8
Create Date: 2024-05-15 20:32:47.355869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a242f8a7ce1'
down_revision: Union[str, None] = 'e0f94e9a45b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
