# ORM Relationships

## Goal
Implement a one-to-many relationship between two ORM models using ForeignKey and relationship.  
Understand how SQLAlchemy manages bidirectional associations and persistence.

## What was done
Defined User and Post models with ForeignKey and back_populates.  
Implemented relationship on both sides and tested object persistence through Session.  
Verified automatic user_id assignment and lazy loading behavior.

## Notes
relationship works on the Python level while ForeignKey works on the database level.  
Related objects are persisted automatically due to cascade behavior.  
Lazy loading triggers additional queries when accessing related objects.