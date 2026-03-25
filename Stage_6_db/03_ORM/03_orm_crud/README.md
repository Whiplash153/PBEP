# CRUD with SQLAlchemy ORM

## Goal
Learn how to perform basic CRUD operations using SQLAlchemy ORM.
Understand how Session manages database transactions.

## What was done
Implemented Create, Read, Update and Delete operations using SQLAlchemy Session.
Worked with ORM models instead of raw SQL queries.
Used commit to persist changes in the database.

## Notes
Session controls transactions and tracks object changes.
Read operations do not require commit.
Update and Delete operations require commit to persist changes.