"""seed review with test data

Revision ID: f52f04fab0db
Revises: 99a99c9524cc
Create Date: 2026-03-18 11:37:37.904521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone


# revision identifiers, used by Alembic.
revision: str = 'f52f04fab0db'
down_revision: Union[str, Sequence[str], None] = '99a99c9524cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    now = datetime.now(timezone.utc)
    op.bulk_insert(
        sa.table(
            'reviews',
            sa.column('product_id'),
            sa.column('text'),
            sa.column('rating'),
            schema='core'
        ),
        [
            {'product_id': 2, 'text': 'good', 'rating': 5},
            {'product_id': 3, 'text': 'bad', 'rating': 2},
            {'product_id': 4, 'text': 'worst', 'rating': 1}
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        "DELETE FROM core.reviews WHERE product_id IN (2, 3, 4)"
    )
