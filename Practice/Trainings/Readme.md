# Task Manager (Level 1)

## Goal
Build a small but complete program that manages tasks as persistent entities.
The goal was to move from in-memory exercises to a program with state, rules, and lifecycle.

## What was done
Implemented a task model with explicit state and stable identifiers.
Separated business logic from storage by introducing a JSON-based storage layer.
Added persistence so tasks survive program restarts.
Used domain errors to enforce rules inside objects instead of external checks.
Created a simple CLI layer to exercise the system without mixing it with logic.

## Notes
The program is focused on behavior and boundaries, not on user interface quality.
Storage is the single source of truth and fully owns loading and saving data.
Errors are used as contracts to protect object invariants.
The project intentionally avoids tests and infrastructure, as this is a Level 1 program.