# Approval System (L2)

## Goal

This project implements a basic approval system where users can create proposals, assign participants, and collect votes to reach a final decision.

The system models a controlled decision-making process with clear states, transitions, and constraints.

---

## What was done

- Implemented proposal creation with participants validation
- Implemented voting system with domain constraints
- Added proposal lifecycle: draft → voting → approved / rejected
- Implemented both automatic and manual proposal finishing
- Added domain-level validations and custom exceptions
- Implemented layered architecture (router / service / repository)
- Added database layer using SQLAlchemy ORM
- Implemented API using FastAPI
- Covered core logic and API with pytest tests

---

## Architecture

The project follows a layered architecture:

- **Router (FastAPI)** — handles HTTP requests and responses
- **Service layer** — contains business logic and enforces rules
- **Repository layer** — handles database interactions
- **Models (ORM)** — define database structure and relationships
- **Schemas (Pydantic)** — define request/response formats

This separation ensures that business logic is isolated from HTTP and database layers.

---

## Business Logic

The system enforces the following rules:

- Only the proposal author can start or finish voting
- Only assigned participants can vote
- Each participant can vote only once
- Voting is allowed only in "voting" status
- Proposal automatically finishes when all participants have voted
- Proposal can also be finished manually by the author
- Final status is determined by majority of votes:
  - approve > reject → approved
  - otherwise → rejected

---

## API Overview

Main endpoints:

- `POST /proposals` — create proposal
- `GET /proposals/{id}` — get proposal
- `POST /proposals/{id}/start` — start voting
- `POST /votes` — submit vote
- `POST /proposals/{id}/finish` — finish proposal manually
- `GET /proposals/{id}/result` — get result

---

## Error Handling

Custom domain errors are used and mapped to HTTP responses:

- 400 — validation errors (invalid input)
- 403 — forbidden actions (not participant / not author)
- 404 — entity not found
- 409 — invalid state or conflicting action

---

## Limitations (L2)

The system intentionally does NOT include:

- Authentication and authorization system
- No user interface (UI), backend API only
- User roles
- Voting deadlines
- Multi-stage approval workflows
- Advanced voting strategies (weight, veto, quorum)

This version represents a simplified L2 baseline for further extension.

---

## Run

1. Update DATABASE_URL in app/db/session.py
2. Create database (e.g. `approve_db`)
3. Manually run database initialization script (app/db/db_init.py)
4. Run: uvicorn app.main:app --reload 
5. Open Swagger UI: http://127.0.0.1:8000/docs
