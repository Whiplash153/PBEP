# FastAPI Pydantic Models

## Goal
Learn how to use Pydantic models for request validation and data structure control in FastAPI.

## What was done
Created data models using Pydantic BaseModel.  
Implemented POST endpoints with automatic validation.  
Added optional fields using default values.  
Extended models with validation rules using Field (length ограничения, числовые ограничения).  
Tested API behavior and validation using Swagger UI.

## Notes
Pydantic converts JSON into Python objects automatically.  
Fields can be required or optional depending on default values.  
Validation rules (min_length, gt, ge) are defined using Field.  
Invalid data returns a 422 error with detailed explanation.  
Models allow controlling API input without manual checks.