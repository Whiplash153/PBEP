Architecture and design notes

This project is a CLI application corresponding to Level 1.

General principles

- clear separation of responsibilities
- explicit object state
- stable entity identifiers
- single source of truth for data
- no business logic inside CLI

cli.py

Responsible only for:
- user interaction (input / output)
- selecting user scenarios
- calling storage and model methods

CLI does not contain business rules and does not make decisions.

models.py

Contains the HomeTask model.

Model responsibilities:
- store its own state (id, title, responsible, is_closed)
- validate allowed actions
- protect invariants (for example, a task cannot be closed twice)

The model does not know where or how it is stored.

storage.py

Acts as the single source of truth for all data.

Responsible for:
- keeping tasks in memory
- loading tasks from JSON on startup
- saving tasks to JSON after changes
- returning the list of tasks
- finding a task by ID
- generating new unique IDs

No other part of the program works with the file directly.

logic.py

A layer for business rules that:
- do not belong to a single model
- require external context checks

At the current level it is used minimally, but it is present for architectural clarity and future growth.

Program level

The program fully meets Level 1 requirements:
- user scenario via CLI
- data survives restarts
- stable entity IDs
- separation between model, storage, and interface
- code is designed for further extension

Deliberate limitations

At this level the program intentionally does not include:
- tests
- roles and permissions
- API
- complex workflows

These aspects are planned for Level 2.