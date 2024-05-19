"""update Sale relation

Revision ID: af49879f8193
Revises: e12fe636c20d
Create Date: 2024-05-19 22:30:55.895834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af49879f8193'
down_revision: Union[str, None] = 'e12fe636c20d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
