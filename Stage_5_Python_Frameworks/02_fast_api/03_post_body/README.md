# FastAPI POST and Body

## Goal
Learn how to handle POST requests and receive data from request body.

## What was done
Created a POST endpoint that accepts JSON data as a dictionary.  
Implemented a GET endpoint that returns a list of products.  
Tested endpoints using Swagger UI.

## Notes
POST requests send data in the request body, while GET requests retrieve data.  
FastAPI automatically converts JSON into Python dictionaries.  
The current implementation does not store data, so GET always returns an empty list.