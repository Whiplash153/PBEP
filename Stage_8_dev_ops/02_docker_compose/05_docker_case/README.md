# Docker Compose Case

## Goal

Containerize the existing FastAPI project so that the entire application can be started with a single Docker Compose command.

The final solution should run:

- FastAPI
- PostgreSQL
- Docker Network
- Docker Volume
- Alembic
- Shared `.env` configuration

---

# Implementation

## Backend

Created a Dockerfile for the application.

The container:

- installs dependencies;
- copies the project source code;
- starts FastAPI with Uvicorn.

---

## PostgreSQL

PostgreSQL runs in a separate container.

Database credentials are configured through environment variables.

---

## Docker Compose

Created `docker-compose.yml`.

It starts both services:

- backend;
- postgres.

Compose also automatically creates:

- a shared Docker network;
- a persistent volume for PostgreSQL.

---

## Shared .env

Both the application and Alembic use the same configuration source.

The following variable is shared:

```text
DATABASE_URL
```

It is used by:

- FastAPI;
- Alembic.

The database URL is no longer duplicated inside `alembic.ini`.

---

## Alembic

`alembic/env.py` was updated to load the database connection string from `.env`.

As a result:

```
.env
   │
   ├──► FastAPI
   └──► Alembic
```

Both components now use a single source of truth.

---

# Problems Encountered

## 1. localhost inside Docker

Initially the application attempted to connect to:

```
localhost
```

Inside a container, `localhost` refers to the container itself rather than the PostgreSQL container.

The issue was fixed by replacing the host with the Compose service name:

```
postgres
```

---

## 2. Broken migration history

The original baseline migration contained only:

```python
def upgrade():
    pass
```

The following migration attempted to modify the `audit_log` table before it had been created.

This resulted in the error:

```
relation "audit_log" does not exist
```

---

## Solution

The migration history was recreated.

A new baseline migration:

```
0001_baseline_schema.py
```

was created to generate the complete database schema from scratch.

---

## 3. Docker build cache

After removing the old migrations, Docker continued using the previous image.

The backend image was rebuilt without cache:

```bash
docker compose build --no-cache backend
```

A `.dockerignore` file was also added to exclude unnecessary files such as:

- `.git`
- `__pycache__`
- `.venv`
- `.env`
- `.pytest_cache`

---

# Validation

The following was successfully verified:

- FastAPI starts correctly;
- PostgreSQL starts correctly;
- Alembic applies migrations;
- all database tables are created;
- PostgreSQL data persists after container restarts.

After running:

```bash
docker compose down
docker compose up
```

the `alembic_version` table still contained:

```
0001
```

confirming that the Docker volume preserved the database state.

---

# Common Commands

Start the application

```bash
docker compose up --build
```

Stop containers

```bash
docker compose down
```

Remove containers and database volume

```bash
docker compose down -v
```

Create a new migration

```bash
docker compose exec backend alembic revision --autogenerate -m "..."
```

Apply migrations

```bash
docker compose exec backend alembic upgrade head
```

Show migration history

```bash
docker compose exec backend alembic history
```

Show current revision

```bash
docker compose exec backend alembic heads
```

Connect to PostgreSQL

```bash
docker compose exec postgres psql -U shelby -d approve_db
```

---

# Result

The project is fully containerized.

A single Docker Compose command starts:

- FastAPI;
- PostgreSQL;
- Docker networking;
- persistent storage via Docker Volumes.

Alembic runs inside the backend container and both the application and Alembic use a shared `.env` configuration.