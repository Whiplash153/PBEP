# CD Deployment

## Goal

Configure automatic deployment of a Dockerized FastAPI application to a VPS after successful CI completion.

The goal is to remove manual deployment steps and make GitHub Actions automatically deliver and run new application versions.

---

## What was done

Created a CD pipeline that automatically:

1. Waits for successful CI completion.
2. Connects to the VPS through SSH.
3. Pulls the latest Docker image from GitHub Container Registry.
4. Updates application containers using Docker Compose.

---

## Full Pipeline

```
Developer

↓

git push

↓

GitHub Repository

↓

GitHub Actions Runner

↓

CI Pipeline:
- install dependencies
- start PostgreSQL service
- run migrations
- run tests
- build Docker image
- push image to GHCR

↓

GitHub Container Registry (GHCR)

↓

CD Pipeline:
- connect to VPS through SSH
- docker pull
- docker compose up -d

↓

VPS Server

↓

Docker Container

↓

Running Application
```

---

## Workflow Structure

The workflow contains two jobs:

```
tests

↓

deploy
```

The deploy job starts only after successful completion of the CI job.

Implemented with:

```yaml
needs: tests
```

If tests fail, deployment does not start.

---

## CI Job

The CI job validates the application and creates a Docker image.

Process:

```
Source Code

↓

Install Dependencies

↓

Prepare Database

↓

Run Migrations

↓

Run Tests

↓

Build Docker Image

↓

Push Image to GHCR
```

Result:

A ready-to-run Docker image is stored in GitHub Container Registry:

```
ghcr.io/whiplash153/approval-api:latest
```

---

## CD Job

The CD job delivers the prepared application to the VPS.

Commands executed on the server:

```bash
cd /opt/apps/cicd_l3

docker pull ghcr.io/whiplash153/approval-api:latest

docker compose up -d
```

Process:

1. Connect to the VPS.
2. Navigate to the application directory.
3. Download the latest Docker image.
4. Recreate containers with the updated image.
5. Start the new application version.

---

## SSH Deployment

GitHub Actions connects to the VPS using SSH.

Required GitHub Secrets:

```
SERVER_HOST
SERVER_USER
SSH_PRIVATE_KEY
```

Secrets are stored separately from the repository code.

They are injected into the workflow using:

```yaml
${{ secrets.SECRET_NAME }}
```

---

## VPS Structure

The VPS contains two independent application versions:

```
VPS

├── approval-system
│
│   Old L3 version
│   Port: 8001
│
└── cicd_l3
    │
    New CD deployment
    Port: 8002
```

They use separate:

- containers;
- ports;
- Docker networks;
- PostgreSQL volumes.

---

## Important Concepts

### Runner

A temporary computer provided by GitHub Actions.

The runner executes workflow commands:

- installs dependencies;
- runs tests;
- builds Docker images;
- performs deployment.

The runner is deleted after workflow completion.

---

### Registry

A storage location for Docker images.

It allows one machine to build an image and another machine to download it.

Flow:

```
GitHub Actions Runner

↓

Docker Image

↓

GHCR

↓

VPS
```

---

### Docker Image

A packaged version of an application.

Contains:

- application code;
- dependencies;
- runtime configuration.

An image itself is not running.

To run the application:

```
Docker Image

↓

Docker Container
```

---

### Docker Container

A running instance created from a Docker image.

The container executes the application and handles user requests.

---

## Result

A complete automatic deployment flow is working:

```
git push

↓

GitHub Actions

↓

CI Tests

↓

Docker Build

↓

GHCR

↓

SSH Connection

↓

VPS

↓

Docker Compose

↓

Updated Container
```

Manual deployment through SSH is no longer required.