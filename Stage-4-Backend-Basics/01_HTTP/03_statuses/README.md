# Goal
Understand how HTTP status codes reflect the result of a server processing a request.  
Learn the core groups of codes (1xx–5xx) and the most common individual statuses used in real applications.

# What was done
Three scenarios were described:
1. Successful creation of a new resource  
2. Client sending invalid data  
3. Requesting a resource that does not exist  

For each scenario, the correct HTTP status code was chosen and printed together with a short explanation of its meaning.

# Notes
- 201 indicates successful creation of a resource (typically used after POST).  
- 400 is returned when the client provides malformed or invalid input.  
- 404 is used when a requested resource cannot be found.  