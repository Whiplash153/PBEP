# ORM Model with SQLAlchemy

## Goal
Create an ORM model that describes a database table using SQLAlchemy.  
Understand how Python classes are mapped to database tables.

## What was done
A declarative base was created using SQLAlchemy.  
A Product model was defined with multiple columns including primary key, constraints, default values and nullable fields.  
The model structure replicates a typical SQL table using ORM mapping.

## Notes
Each class attribute represents a column in the database table.  
Column parameters define constraints such as primary key, uniqueness, default values and nullability.  
The ORM model allows database structure to be defined directly in Python.