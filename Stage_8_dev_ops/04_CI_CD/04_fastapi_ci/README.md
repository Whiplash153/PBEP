# FastAPI CI

## Goal

Configure Continuous Integration for a real FastAPI application.

The goal is to automatically verify that the application works correctly after every code change.

---

## What was done

Created a GitHub Actions workflow for the FastAPI project.

The workflow automatically:

1. Starts after pushing code to the repository.
2. Creates a clean Ubuntu testing environment.
3. Installs project dependencies.
4. Starts PostgreSQL database.
5. Applies Alembic migrations.
6. Runs pytest tests.

---

## CI Pipeline

The pipeline:

Developer pushes code

↓

GitHub Actions starts

↓

Create testing environment

↓

Install dependencies

↓

Start PostgreSQL service

↓

Apply database migrations

↓

Run pytest

↓

Success or failure result

---

## Project Integration

The CI pipeline was configured for a FastAPI application using:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- pytest
- Poetry

---

## Database Setup

GitHub Actions creates a temporary PostgreSQL service for testing.

Before running tests:

1. PostgreSQL starts.
2. Database connection becomes available.
3. Alembic creates required tables.
4. Tests run against the prepared database.

---

## Environment Variables

The application requires database connection variables:

DATABASE_URL

TEST_DATABASE_URL

These variables are provided through the GitHub Actions environment.

Sensitive information is not stored in the repository.

---

## Workflow Structure

The workflow contains:

- push trigger;
- GitHub runner configuration;
- PostgreSQL service;
- dependency installation;
- migration execution;
- test execution.

Workflow location:

.github/

└── workflows/

    └── ci.yml

---

## Result

After completing this task:

- FastAPI project is automatically tested after code changes.
- Database environment is created automatically.
- Database migrations are applied before tests.
- Broken code is detected before deployment.

The project now has a working CI pipeline.