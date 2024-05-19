"""ceate relationships between Product and Sales

Revision ID: 87dadc767090
Revises: 36a43fe57d61
Create Date: 2024-05-20 01:02:00.714844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87dadc767090'
down_revision: Union[str, None] = '36a43fe57d61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
