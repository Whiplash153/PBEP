# Docker Compose — Compose Network

## Goal

Understand how Docker Compose containers discover and communicate with each other using service names instead of IP addresses.

## What Was Done

- Learned how Docker Compose automatically creates a shared network.
- Added a PostgreSQL service to `docker-compose.yml`.
- Configured a SQLAlchemy connection.
- Replaced `localhost` with the PostgreSQL service name (`postgres`) in the connection string.
- Created a simple connection test in `test_connection.py`.
- Executed the SQL query `SELECT 1`.
- Verified that the backend successfully connected to PostgreSQL through the Docker Compose network.

## What I Learned

- Docker Compose automatically creates a private network for all services.
- Every service receives a DNS name equal to its service name in `docker-compose.yml`.
- The backend connects to PostgreSQL using the service name instead of an IP address.
- The hostname `postgres` exists only inside the Docker Compose network.
- Outside Docker Compose, applications typically connect using `localhost`.

## Practical Example

Connection string:

```text
postgresql+psycopg2://postgres:postgres@postgres:5432/sandbox
```

Meaning:

- `postgresql+psycopg2` — PostgreSQL driver.
- `postgres:postgres` — username and password.
- `postgres` — Docker Compose service name.
- `5432` — PostgreSQL internal port.
- `sandbox` — database name.

## Artifacts

- `session.py`
- `test_connection.py`
- `docker-compose.yml`

## Result

The backend successfully connected to PostgreSQL using the service name `postgres`, executed `SELECT 1`, and received the expected result. This confirmed that Docker Compose networking and service discovery were working correctly.