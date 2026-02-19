# REST API – Status Codes

## Goal
Understand how HTTP status codes represent the real outcome of REST operations and how they form a contract between client and server.

## What was done
Studied and analyzed HTTP status codes for core REST methods (GET, POST, PUT, PATCH, DELETE) through scenario-based diagnostics.
Focused on distinguishing between request validity issues (400), missing resources (404), successful operations (200), resource creation (201), and successful actions without response body (204).

Instead of implementing a server, the task was completed by mapping real-world REST scenarios to correct HTTP responses and validating the logic through edge cases and traps.

## Notes
HTTP status codes describe the result of an operation, not the intent of the request.
A request can be valid but still return 404 if the resource does not exist.
POST creates resources and returns 201 on success, while PUT and PATCH update existing resources and return 200.
DELETE returns 204 when the resource is successfully removed and no response body is required.