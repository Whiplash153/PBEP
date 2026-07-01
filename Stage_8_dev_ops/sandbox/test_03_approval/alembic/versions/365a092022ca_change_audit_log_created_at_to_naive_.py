"""change audit log created_at to naive datetime

Revision ID: 365a092022ca
Revises: 755bed27761e
Create Date: 2026-06-02 15:05:50.050312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '365a092022ca'
down_revision: Union[str, Sequence[str], None] = '755bed27761e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'audit_log',
        'created_at',
        existing_type=sa.DateTime(timezone=True),
        type_=sa.DateTime()
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'audit_log',
        'created_at',
        existing_type=sa.DateTime(),
        type_=sa.DateTime(timezone=True)
    )
