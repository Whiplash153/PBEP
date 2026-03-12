# ORM Case — Mini Backend

## Goal
Build a small backend-style system using SQLAlchemy ORM with PostgreSQL.  
Implement models, relationships, transactional CRUD operations, and cascade delete behavior.  

## What was done
Configured engine and metadata, defined User and Order models with one-to-many relationship.  
Implemented a separate CRUD layer without transaction control inside functions.  
Tested create, read, update, and delete operations with centralized transaction management.  

## Notes
Flush is required to obtain primary key values before dependent inserts within the same transaction.  
Cascade configuration must be defined both at ORM level and database level to avoid integrity errors.  
`create_all()` does not modify existing tables; schema changes require recreation or migrations.  