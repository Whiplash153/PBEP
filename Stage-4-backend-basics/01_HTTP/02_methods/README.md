# Goal
Understand how different HTTP methods are used to interact with resources:
- GET for retrieving data,
- POST for creating new items,
- PATCH for partial updates of existing items.

# What was done
Three custom operations were defined:
1. Reading a resource (GET)
2. Creating a new resource (POST)
3. Updating part of an existing resource (PATCH)

For each operation, the correct HTTP method was chosen and a proper start-line was constructed in the format:
`METHOD PATH HTTP/1.1`

Each start-line was printed to demonstrate how different methods are used in practice.

# Notes
POST always targets a collection (e.g., `/cars`) because the server assigns the ID of a newly created resource.  
PATCH and GET operate on existing items and therefore use paths that include an ID (e.g., `/cars/1`).