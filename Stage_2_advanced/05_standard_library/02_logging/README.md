# Logging (Standard Library)

## Goal
Learn how to use Python's built-in `logging` module for tracking program execution, debugging, and saving event history.

## Overview
This task covers the fundamentals of logging in Python and progresses from basic configuration to multi-handler setups.

### Step 1 — Basic Logging
- Introduced the `logging` module and its basic configuration via `logging.basicConfig()`.
- Learned about log levels and how to display different message types (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

### Step 2 — Log Levels
- Studied how log levels filter messages by importance.
- Demonstrated changing the log level dynamically using `setLevel()`.
- Understood that by default, Python logs only `WARNING` and higher.

### Step 3 — File Handler
- Created a `FileHandler` to save logs into a file (`app.log`).
- Learned about `Formatter` and how to control log message format.
- Differentiated between writing (`"w"`) and appending (`"a"`) modes.

### Step 4 — Multiple Handlers & Formatters
- Configured both `StreamHandler` (console) and `FileHandler` (file) in one logger.
- Applied different formats and levels for each handler.
- Result: console shows only warnings and errors, file logs everything with timestamps.

### Mini Practice
- Combined all concepts into a single working example:
  - Console output limited to warnings and errors.
  - File `service.log` contains the full event history (`DEBUG` and above).
  - Simulated a realistic program workflow from connection setup to shutdown.

## Key Concepts
- `logging.getLogger()`
- `basicConfig()`
- `StreamHandler` and `FileHandler`
- `Formatter`
- Log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- Level-based filtering and multi-handler configuration