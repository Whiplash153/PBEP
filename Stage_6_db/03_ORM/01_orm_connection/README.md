# ORM Connection (SQLAlchemy)

## Goal
The goal of this task was to establish a basic connection between a Python application and a PostgreSQL database using SQLAlchemy.

## What was done
A database connection URL was defined and used to create a SQLAlchemy Engine.  
A connection was opened using the Engine, and a simple SQL query was executed to verify that the application can communicate with the database.

## Notes
SQLAlchemy does not immediately open a database connection when the Engine is created. The connection is established only when the first SQL statement is executed.  
The query result is returned as a result container object, from which rows must be explicitly extracted.