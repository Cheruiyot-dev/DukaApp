"""update Sale relation

Revision ID: 36a43fe57d61
Revises: af49879f8193
Create Date: 2024-05-19 22:34:51.261775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36a43fe57d61'
down_revision: Union[str, None] = 'af49879f8193'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
