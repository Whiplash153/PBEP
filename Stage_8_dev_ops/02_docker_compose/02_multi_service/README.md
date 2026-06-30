# Docker Compose: Backend and PostgreSQL Connection

## Goal

Learn how backend and PostgreSQL communicate inside a Docker Compose project using the internal Docker network.

## What was done

Configured communication between the FastAPI backend and PostgreSQL container. Used the service name as the database host instead of localhost. Verified that both services communicate successfully within the Docker network.

## Notes

Containers in the same Compose project communicate through the automatically created network. Service names act as hostnames inside this network. Localhost refers only to the current container, not to other services.