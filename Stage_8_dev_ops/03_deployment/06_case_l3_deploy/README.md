# Public L3 Deployment

The L3 approval system was deployed on a VPS using Docker Compose.

Stack:
- FastAPI
- PostgreSQL
- Docker
- Docker Compose

Deployment:
- Application runs in Docker containers
- PostgreSQL uses a persistent volume
- Environment variables are stored separately in .env
- API is publicly available through VPS IP

Verification:
- Containers restart successfully after docker compose down/up
- Swagger UI is available at /docs
