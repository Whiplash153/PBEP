# PBEP — Python Backend Educational Program

PBEP is a structured program for learning Python backend development. This repository records the progression from Python fundamentals to building, testing, containerizing, and deploying backend applications. It contains study notes, focused exercises, integration cases, sandboxes, and progressively more complete programs rather than a single application.

## Program stages

The numbering follows the original curriculum and the repository layout.

- **[Stage 1 — Python basics](./Stage_1_basics/):** syntax, built-in data structures, functions and modules, exceptions, object-oriented programming, files, and virtual environments.
- **[Stage 2 — Advanced Python](./Stage_2_advanced/):** data-model methods, iterators and generators, decorators and context managers, asynchronous I/O, selected standard-library tools, and dependency management with Poetry and Pipenv.
- **Stage 3 — Git and collaborative development:** Git workflows, GitHub repositories, issues and pull requests, and Markdown documentation. This stage was completed through practical repository work rather than preserved as a separate lesson directory.
- **[Stage 4 — Backend foundations](./Stage_4_backend/):** HTTP requests and responses, methods, headers and status codes, REST resource design, CRUD semantics, and JSON serialization—first implemented without a web framework.
- **[Stage 5 — Frameworks](./Stage_5_frameworks/):** FastAPI endpoints, path and query parameters, request bodies, Pydantic validation, error handling, and an in-memory CRUD API.
- **[Stage 6 — Databases](./Stage_6_db/):** PostgreSQL access through SQLAlchemy ORM, models and relationships, transactional CRUD, cascade behavior, and schema/data migrations with Alembic.
- **[Stage 7 — Testing](./Stage_7_tests/):** pytest fundamentals, parametrization, fixtures, state isolation, and API-oriented test cases.
- **[Stage 8 — DevOps](./Stage_8_dev_ops/):** Docker and Docker Compose, persistent services and networking, VPS and cloud deployment, and CI/CD with GitHub Actions, GHCR, migrations, tests, and automated delivery.
- **[Stage 9 — Algorithms and data structures](./Stage_9_algorithms/):** an ongoing, separate study track that currently begins with Big O and complexity analysis.

## Main areas and technologies

The work covers Python 3.12, OOP and asynchronous programming; HTTP, REST, JSON, FastAPI and Pydantic; PostgreSQL, SQLAlchemy and Alembic; pytest and HTTP-focused testing; Poetry and Pipenv; and Docker, Docker Compose, GitHub Actions, GHCR, and VPS deployment. The examples also apply layered design, separation of business logic from I/O, explicit state transitions, domain errors, persistence, migrations, transaction boundaries, and concurrency protection.

## How the practice is organized

The program follows a consistent progression: stage → topic → task → guided steps → independent mini-practice → integration case. Most topics live in small, self-contained directories with code and a short English README recording the goal, implementation, and important notes. [`Practice`](./Practice/) adds free-form tasks, repeated solution patterns, training exercises, and safe sandboxes. [`Programs`](./Programs/) contains larger applications that evolve from JSON-backed CLI tools to a layered database-backed API.

This structure preserves the learning process as well as its results: isolated concepts are implemented first, then integrated into larger systems and finally exercised through testing, containerization, and deployment.

## Selected final projects

- **[Approval System](https://github.com/Whiplash153/approval-system)** — a FastAPI/PostgreSQL REST API for proposal workflows and voting, with layered architecture, Alembic migrations, audit logging, transactional concurrency handling, pytest coverage, Docker Compose, and CI/CD deployment.
- **[TG Food Bot](https://github.com/Whiplash153/TG_food_bot)** — a portfolio Telegram bot that serves company content, collects contact requests in PostgreSQL, and notifies a manager; built with `python-telegram-bot`, SQLAlchemy, Alembic, Poetry, Docker Compose, and a VPS `systemd` deployment.

## Current status

The main Python backend curriculum and its final projects are complete. Algorithms and data structures continue separately as an ongoing study track.
