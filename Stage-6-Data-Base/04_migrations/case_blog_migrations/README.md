# Case: Blog Migrations

## Goal
Apply all migration techniques (autogeneration, manual adjustments, data seeding) in a complete cycle for a simple blog model with `Post` and `Comment`.

## What was done
- Created a new database `blog_db` and schema `core` owned by user `msh`
- Defined SQLAlchemy models for `Post` and `Comment` with relationships and cascade delete
- Configured Alembic from scratch in a separate `case_blog_migrations` folder
- Generated and applied the first migration to create both tables
- Created a seed migration to insert test posts and comments
- Solved a foreign key issue in the seed migration by retrieving generated post IDs dynamically
- Verified the upgrade/downgrade cycle works without data corruption

## Notes
- Models must reflect the actual table structure; any change should start with the model.
- Autogeneration (`--autogenerate`) is a powerful tool but should always be reviewed.
- Seeding data in migrations requires careful handling of auto-incrementing IDs.
- Always implement both `upgrade()` and `downgrade()` to keep migrations reversible.
- Using `op.get_bind()` allows executing raw SQL queries inside a migration to fetch generated IDs.