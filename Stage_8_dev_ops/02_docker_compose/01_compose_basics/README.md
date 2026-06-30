# Docker Compose: Compose Basics

## Goal

Learn how to manage multiple containers using Docker Compose and run application services as a single project.

## What was done

Created a Docker Compose configuration for a FastAPI application and a PostgreSQL database. Configured services, ports, environment variables and a named volume. Verified that both containers start together and that PostgreSQL data persists after container recreation.

## Notes

Docker Compose automatically creates a network for project services. A named volume stores database files independently of the container lifecycle. Service configuration and shared project resources are defined separately in the compose file.