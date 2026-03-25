# Task 1: Alembic Setup and First Migration

## Goal
Set up Alembic in an existing project, configure it to work with PostgreSQL, and create the first automatic migration based on SQLAlchemy models.

## What was done
- Installed Alembic via Poetry
- Initialized Alembic with `alembic init alembic`
- Configured database URL in `alembic.ini` to connect to `mig_shop`
- Adjusted `env.py` to import `Base` from `models.py` and set `target_metadata`
- Fixed permission issues by configuring Alembic to use the `core` schema
- Generated the first migration with `--autogenerate` based on the `Product` model
- Applied the migration using `alembic upgrade head`, creating the `products` table

## Notes
- Alembic stores migration history in the `alembic_version` table.
- The `core` schema must exist and be accessible by the database user.
- Autogeneration compares the current database state with model metadata; it works best when the database is empty or fully migrated.
- Manual intervention in `env.py` is often needed to handle schemas, multiple databases, or custom import paths.