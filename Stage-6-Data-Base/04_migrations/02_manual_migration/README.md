# Task 2: Manual Migration Creation

## Goal
Learn to create and apply database migrations manually without autogeneration, understanding the internal structure of migration files and the upgrade/downgrade cycle.

## What was done
- Created an empty revision using `alembic revision`
- Manually wrote `upgrade()` and `downgrade()` functions to create and drop a `reviews` table with a foreign key to `products`
- Applied the migration and verified the table structure in PostgreSQL
- Rolled back the migration using `downgrade -1` and confirmed the table was removed
- Reapplied the migration to restore the table
- Repeated the process for a `comments` table as an independent exercise

## Notes
- Manual migrations give full control over DDL and are necessary for complex schema changes.
- Always implement both `upgrade()` and `downgrade()` to ensure reversibility.
- Foreign keys must reference tables with schema prefix (e.g., `core.products.id`).
- The `op` object provides database-agnostic operations; `sa.types` ensure type compatibility across DB engines.
- Default values like `CURRENT_TIMESTAMP` are set using `server_default=sa.text('CURRENT_TIMESTAMP')`.