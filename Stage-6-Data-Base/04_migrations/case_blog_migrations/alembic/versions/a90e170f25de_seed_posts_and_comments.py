"""seed posts and comments

Revision ID: a90e170f25de
Revises: 063d19001786
Create Date: 2026-03-19 11:46:42.180393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, DateTime

# revision identifiers, used by Alembic.
revision: str = 'a90e170f25de'
down_revision: Union[str, Sequence[str], None] = '063d19001786'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Создаем объекты таблиц для работы с метаданными
    posts_table = table('posts',
                        column('id', Integer),
                        column('title', String),
                        column('content', String),
                        column('created_at', DateTime),
                        column('views', Integer),
                        schema='core'
                        )
    comments_table = table('comments',
                           column('post_id', Integer),
                           column('author', String),
                           column('text', String),
                           column('created_at', DateTime),
                           schema='core'
                           )

    now = datetime.now(timezone.utc)

    # 1. Вставляем посты
    op.bulk_insert(
        posts_table,
        [
            {'title': 'First post', 'content': 'Hello world!', 'created_at': now, 'views': 0},
            {'title': 'Second post', 'content': 'Alembic is cool', 'created_at': now, 'views': 0},
        ]
    )

    # 2. Получаем ID вставленных постов, выполняя SQL-запрос.
    # Соединение с БД в контексте миграции уже открыто.
    connection = op.get_bind()
    result = connection.execute(
        sa.text("SELECT id, title FROM core.posts WHERE title IN ('First post', 'Second post')")
    ).fetchall()

    # Создаем словарь: {'First post': id1, 'Second post': id2}
    post_ids = {title: id for id, title in result}

    # 3. Вставляем комментарии, используя реальные ID постов
    op.bulk_insert(
        comments_table,
        [
            {'post_id': post_ids['First post'], 'author': 'Alice', 'text': 'Great post!', 'created_at': now},
            {'post_id': post_ids['First post'], 'author': 'Bob', 'text': 'Thanks for sharing', 'created_at': now},
            {'post_id': post_ids['Second post'], 'author': 'Charlie', 'text': 'Alembic is indeed cool',
             'created_at': now},
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM core.comments")
    op.execute("DELETE FROM core.posts")
