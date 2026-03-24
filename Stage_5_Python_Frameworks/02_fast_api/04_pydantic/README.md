# FastAPI Pydantic Models

## Goal
Learn how to use Pydantic models for request validation and structured data handling.

## What was done
Created a User model using Pydantic BaseModel.  
Implemented a POST endpoint to receive and validate user data.  
Implemented a GET endpoint to return a list of users.  
Tested endpoints using Swagger UI.

## Notes
Pydantic models provide automatic validation and type checking.  
FastAPI converts JSON into Python objects and обратно в JSON автоматически.  
Missing or invalid fields result in a 422 error.  
Using models is safer and cleaner than working with raw dictionaries.