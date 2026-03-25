# Task 4: Seeding Data with Migrations

## Goal
Learn to insert and delete data within migrations using `op.bulk_insert` and `op.execute`, ensuring that seed data is versioned alongside schema changes.

## What was done
- Created a migration to seed the `products` table with test data (Notebook, Mouse, Keyboard)
- Used `op.bulk_insert` with explicit `created_at` and `updated_at` values to satisfy `NOT NULL` constraints
- Implemented `downgrade()` to delete only the seeded rows via `DELETE ... WHERE name IN (...)`
- Verified data insertion and removal by upgrading and downgrading
- Created an additional migration to seed the `reviews` table with sample reviews linked to existing products
- Ensured all operations are reversible and schema-qualified (`core.products`, `core.reviews`)

## Notes
- `op.bulk_insert` operates at the SQL level, bypassing ORM defaults; all `NOT NULL` columns must be provided explicitly.
- `server_default` or explicit values in the migration are required for columns without database-side defaults.
- Always use schema prefixes (`core.table_name`) in raw SQL executed via `op.execute`.
- For rollback, delete by a stable condition (e.g., product names or IDs) rather than relying on auto-generated primary keys.
- Seeding via migrations keeps development, test, and staging environments in sync.