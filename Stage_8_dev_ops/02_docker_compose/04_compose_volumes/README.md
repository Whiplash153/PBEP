# Docker Compose — Compose Volumes

## Goal

Understand how Docker Compose Volumes preserve PostgreSQL data between container recreations.

## What Was Done

- Configured a named Volume in `docker-compose.yml`.
- Connected the Volume to PostgreSQL data directory.
- Started PostgreSQL using Docker Compose.
- Created a test table.
- Inserted a test record.
- Verified the stored data.
- Removed the containers with `docker compose down`.
- Started the application again with `docker compose up`.
- Verified that the table and data were still available.

## What I Learned

- A Volume is independent from a container.
- Containers can be removed without losing data stored in a Volume.
- PostgreSQL continues working with the same database after container recreation.
- Docker mounts the Volume into a directory inside the container.
- The application does not know whether it is writing to a normal directory or to a mounted Volume.

## Practical Example

Volume configuration:

```yaml
services:
  postgres:
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Meaning:

- `postgres_data` — named Docker Volume.
- `/var/lib/postgresql/data` — PostgreSQL data directory inside the container.
- Docker mounts the Volume into this directory before PostgreSQL starts.

## Experiment

1. Created a table:

```sql
CREATE TABLE test_volume (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

2. Inserted a record:

```sql
INSERT INTO test_volume (name)
VALUES ('Hello Volume');
```

3. Verified the data:

```sql
SELECT * FROM test_volume;
```

4. Removed all containers:

```bash
docker compose down
```

5. Started the project again:

```bash
docker compose up
```

6. Executed the same query and confirmed that the data was still present.

## Artifacts

- `docker-compose.yml`

## Result

The PostgreSQL container was recreated, but the database remained unchanged because the data was stored in a Docker Volume instead of the container's filesystem. PostgreSQL detected the existing database and skipped initialization, confirming that the data persisted between container recreations.