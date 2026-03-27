# FastAPI Mini User API

## Goal
Build a simple API service using FastAPI and Pydantic.

## What was done
Implemented basic CRUD operations for users.  
Used Pydantic models for validation.  
Added status codes and error handling.  
Stored data in memory using a list.

## Notes
Each user has an auto-generated id.  
Validation is handled by Pydantic (422 errors).  
Business logic errors return 400/404 using HTTPException.  
Data is stored in memory and resets on server restart.