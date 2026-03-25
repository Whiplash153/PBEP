# FastAPI Status and Errors

## Goal
Learn how to control HTTP responses and handle errors in FastAPI.

## What was done
Implemented POST endpoint with custom status codes.  
Used HTTPException to handle business logic errors.  
Separated automatic validation (Pydantic) from manual error handling.  
Tested API responses using Swagger.

## Notes
Successful POST requests should return 201 Created.  
HTTPException is used to manually raise errors with custom status codes.  
Pydantic handles validation errors automatically (422).  
Business logic errors should be handled separately (400).