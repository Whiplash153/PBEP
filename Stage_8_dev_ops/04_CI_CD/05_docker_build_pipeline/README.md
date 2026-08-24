# Docker Build Pipeline

## Goal

Learn how to automatically build Docker images inside a CI pipeline.

The goal is to understand how application code is transformed into a Docker image after successful checks and how this image is stored in a container registry.

---

## What was done

Created a Docker build stage in GitHub Actions workflow.

The pipeline now automatically:

1. Runs application tests.
2. Builds a Docker image.
3. Authenticates in GitHub Container Registry.
4. Tags the Docker image for registry storage.
5. Pushes the image to GHCR.

---

## CI/CD Pipeline

Current workflow:

```
Developer pushes code

↓

GitHub Actions starts

↓

Create clean Ubuntu runner

↓

Install Python environment

↓

Install dependencies

↓

Start PostgreSQL service

↓

Run migrations

↓

Run tests

↓

Build Docker image

↓

Login to GitHub Container Registry

↓

Tag Docker image

↓

Push image to GHCR
```

---

## Docker Build

Docker image is created using:

```bash
docker build -t approval-api:latest .
```

The command creates an application image from Dockerfile.

Image structure:

```
Dockerfile

↓

Docker Image

↓

Container
```

Important:

Image is not a running application.

It is a template that can be used to create containers.

---

## GitHub Actions Runner

Docker image is built inside GitHub Actions Runner.

The runner is a temporary virtual machine.

During workflow execution:

```
GitHub Runner

    creates

approval-api:latest

    after workflow

Runner is deleted
```

Therefore the image needs to be stored externally.

---

## Docker Registry

Registry is a storage for Docker images.

Used:

```
GitHub Container Registry (GHCR)
```

Workflow:

```
GitHub Actions

↓

Docker Image

↓

GHCR

↓

Production Server
```

---

## Authentication

Added permissions:

```yaml
permissions:
  contents: read
  packages: write
```

Purpose:

```
contents: read

Allows workflow to read repository code.


packages: write

Allows workflow to upload Docker images.
```

Authentication uses:

```yaml
${{ secrets.GITHUB_TOKEN }}
```

The token is automatically created by GitHub Actions.

It is not a personal password.

---

## Docker Tag

Before pushing image to registry, image receives a registry name:

```bash
docker tag approval-api:latest ghcr.io/whiplash153/approval-api:latest
```

Tag does not create a copy.

It creates another reference to the same image.

Before:

```
approval-api:latest
```

After:

```
approval-api:latest

ghcr.io/whiplash153/approval-api:latest
```

---

## Docker Push

Image is uploaded to GHCR:

```bash
docker push ghcr.io/whiplash153/approval-api:latest
```

Result:

```
GitHub Container Registry

approval-api
    |
    └── latest
```

The image can now be downloaded from another machine.

---

## Key Concepts

### CI

Continuous Integration:

```
Code

↓

Tests

↓

Validation
```

Checks that changes do not break the application.


### Docker Build Pipeline

Creates a deployable artifact:

```
Code

↓

Docker Image

↓

Registry
```

---

## Learned Commands

```bash
docker build
```

Creates Docker image from Dockerfile.


```bash
docker tag
```

Adds a new name/tag to an existing image.


```bash
docker push
```

Uploads image to Docker Registry.


```bash
docker login
```

Authenticates Docker client in Registry.


```bash
docker images
```

Shows local Docker images.

---

## Result

Created a working Docker Build Pipeline.

The project can now automatically:

- test code;
- build Docker image;
- publish application image to GitHub Container Registry.

Next step:

Create automatic deployment from Registry to a server.