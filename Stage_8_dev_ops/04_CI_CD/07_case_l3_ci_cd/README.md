# CI/CD Pipeline for L3 Project

## Goal

Set up a complete CI/CD pipeline for the FastAPI application.

The pipeline automatically:

- validates the application code;
- runs tests;
- builds a Docker image;
- pushes the image to GitHub Container Registry (GHCR);
- deploys the new version to a VPS server.

---

## Technologies

- GitHub Actions
- Docker
- Docker Compose
- GitHub Container Registry (GHCR)
- SSH deployment
- FastAPI
- PostgreSQL
- Alembic
- Pytest

---

# Pipeline Flow

```
Developer
    |
    | git push
    ↓
GitHub Actions
    |
    ├── CI
    │     |
    │     ├── Install dependencies
    │     ├── Start PostgreSQL
    │     ├── Run migrations
    │     └── Run tests
    |
    ├── Docker Build
    │     |
    │     └── Build application image
    |
    ├── GHCR
    │     |
    │     └── Push Docker image
    |
    └── CD
          |
          ├── Connect to VPS via SSH
          ├── Pull latest repository changes
          ├── Pull latest Docker image
          └── Restart application containers
```

---

# CI Stage

## Dependency Installation

GitHub Actions creates a clean environment and installs project dependencies using Poetry.

Steps:

- checkout repository;
- install Python;
- install Poetry;
- install dependencies from `pyproject.toml`.

---

## Database Setup

A temporary PostgreSQL container is created inside GitHub Actions.

The pipeline:

- starts PostgreSQL;
- applies environment variables;
- waits until database is healthy.

---

## Database Migration

Before running tests:

```bash
alembic upgrade head
```

is executed.

This guarantees that the database schema matches the current application version.

---

## Testing

The pipeline runs:

```bash
pytest
```

If tests fail:

- CI stops;
- Docker image is not built;
- deployment does not start.

---

# Docker Build Stage

After successful tests:

The application image is built:

```bash
docker build -t approval-api:latest .
```

The image contains:

- Python environment;
- Poetry dependencies;
- FastAPI application;
- application startup command.

---

# Registry Stage

The image is uploaded to:

```
ghcr.io/whiplash153/approval-api:latest
```

GitHub Container Registry stores the ready-to-run application image.

The VPS does not build the project anymore.

It only downloads the prepared Docker image.

---

# Deployment Stage

Deployment is performed through SSH.

GitHub Actions connects to the VPS and executes:

```bash
cd /opt/apps/approval-system
git pull
docker pull ghcr.io/whiplash153/approval-api:latest
docker compose up -d
```

The server:

1. updates configuration files;
2. downloads the new Docker image;
3. recreates containers using the new image.

---

# Docker Compose Configuration

Production uses a fixed Docker Compose project name:

```yaml
name: approval-system
```

This keeps the same environment between deployments.

Docker Compose uses the project name to identify:

- containers;
- networks;
- volumes.

Changing the project name creates a separate environment instead of updating the existing one.

---

# Secrets

GitHub Actions uses repository secrets:

```
SERVER_HOST
SERVER_USER
SSH_PRIVATE_KEY
```

They provide secure SSH access to the VPS.

Secrets are stored in GitHub Actions and are not included in the repository.

---

# Deployment Verification

After deployment:

Check running containers:

```bash
docker ps
```

Expected:

```
approval-system-backend-1
approval-system-postgres-1
```

Backend image:

```
ghcr.io/whiplash153/approval-api:latest
```

Health check:

```bash
curl http://SERVER_IP:8001/health
```

Expected response:

```json
{
  "status": "CI/CD deployment works"
}
```

---

# Key Concepts Learned

## CI (Continuous Integration)

Automatic verification of code changes.

Purpose:

- detect problems early;
- keep the main branch stable.

---

## CD (Continuous Deployment)

Automatic delivery of verified changes to production.

Purpose:

- reduce manual deployment;
- make releases predictable.

---

## Registry

A storage system for Docker images.

Examples:

- Docker Hub;
- GitHub Container Registry;
- AWS ECR.

The registry works like a package repository for containers.

---

## Runner

A machine that executes GitHub Actions workflows.

It:

- receives workflow instructions;
- runs commands;
- builds images;
- executes tests.

---

# Result

The L3 application now has a complete automated deployment pipeline:

```
Code change
    ↓
Git push
    ↓
Automated tests
    ↓
Docker image build
    ↓
Image registry
    ↓
Automatic VPS deployment
    ↓
Updated application
```