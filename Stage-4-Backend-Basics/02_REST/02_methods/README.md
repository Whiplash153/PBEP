# REST Methods — CRUD for Articles

## Goal
Understand how REST methods work by implementing basic routing logic using HTTP method and path.  
Practice full CRUD operations on a simple in-memory collection.

## What was done
Implemented routing based on method–path pairs.  
Added GET for collection and single resource, POST for creation, PUT for full replacement, PATCH for partial updates, and DELETE with idempotent behavior.  
Used dictionary merging for PUT and incremental updates for PATCH.  
Handled resource lookup through a helper function returning an object or null-equivalent.

## Notes
PUT replaces the entire resource, while PATCH updates only provided fields.  
DELETE must be idempotent and return the same result when repeated.  
The task simulates REST behavior without frameworks to solidify core CRUD logic.[..](../../..)