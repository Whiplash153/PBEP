# Basic FastAPI Application

## Goal
Create a simple FastAPI application with basic GET endpoints and run it locally.

## What was done
Initialized a FastAPI app and created two GET endpoints: /hello and /status.  
Configured and ran the server using uvicorn with auto-reload enabled.  
Tested endpoints through browser and Swagger UI.

## Notes
FastAPI automatically converts Python dictionaries to JSON responses.  
Swagger UI is generated automatically and can be used to test endpoints.  
The --reload flag allows automatic server restart on file changes.