# HTTP Basics

This section covers the essential elements of the HTTP protocol used by backend services when communicating with clients.

The focus is on understanding the structure of HTTP, interpreting requests, forming responses, and working with headers and status codes.

## What was learned

### 1. HTTP Request Structure
Breakdown of the start line, headers, and body.  
Understanding how clients communicate intent through method, path, and metadata.

### 2. HTTP Methods
Purpose of the main methods:
- GET: retrieve data  
- POST: create new resources  
- PATCH/PUT: modify existing resources  
- DELETE: remove resources  

### 3. Status Codes
Understanding status groups (1xx–5xx) and key codes:
- 200 OK  
- 201 Created  
- 204 No Content  
- 301 Redirect  
- 400 Bad Request  
- 401 Unauthorized  
- 403 Forbidden  
- 404 Not Found  
- 500 Internal Server Error  
- 503 Service Unavailable  

### 4. HTTP Headers
Client and server headers:
- Identifying client intent (Accept, User-Agent, Accept-Language)
- Defining content format (Content-Type, Content-Length)
- Authorization (Authorization, Cookie)
- Cache and connection management (Cache-Control, ETag, Connection)

Practical examples of reading and forming headers were completed.

## Summary
This module forms the foundation necessary for working with real APIs and backend frameworks.  
Understanding how HTTP carries metadata and data is essential before moving to JSON handling, routing, and server frameworks such as FastAPI.