"""seed products with test data

Revision ID: 99a99c9524cc
Revises: 581ba369bf20
Create Date: 2026-03-18 11:19:24.302564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone
now = datetime.now(timezone.utc)


# revision identifiers, used by Alembic.
revision: str = '99a99c9524cc'
down_revision: Union[str, Sequence[str], None] = '581ba369bf20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.bulk_insert(
        sa.table(
            'products',
            sa.column('name'),
            sa.column('price'),
            sa.column('created_at'),
            sa.column('updated_at'),
            schema='core'
        ),
        [
            {'name': 'Notebook', 'price': 1200.00, 'created_at': now, 'updated_at': now},
            {'name': 'Mouse', 'price': 25.50, 'created_at': now, 'updated_at': now},
            {'name': 'Keyboard', 'price': 85.00, 'created_at': now, 'updated_at': now},
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        "DELETE FROM core.products WHERE name IN ('Notebook', 'Mouse', 'Keyboard')"
    )
