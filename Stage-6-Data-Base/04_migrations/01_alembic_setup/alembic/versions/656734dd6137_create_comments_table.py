"""create comments table

Revision ID: 656734dd6137
Revises: 8017cb074c41
Create Date: 2026-03-17 13:10:48.056134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '656734dd6137'
down_revision: Union[str, Sequence[str], None] = '8017cb074c41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('review_id', sa.Integer(), nullable=False),
        sa.Column('author', sa.String(100), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False,
                  server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['review_id'], ['core.reviews.id']),
        sa.PrimaryKeyConstraint('id'),
        schema='core'
    )

def downgrade() -> None:
    op.drop_table('comments', schema='core')
