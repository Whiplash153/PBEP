# CASE — File Logger (Standard Library)

## Goal
Combine Python's `datetime`, `logging`, `pathlib`, and `os` modules to create an automated daily logging system.

## Overview
This case integrates four standard library modules into one functional mini-project.  
The program automatically creates a new log file for each day, records events, and removes outdated logs.

### Logic
1. Determine the current date with `datetime`.
2. Create a folder `logs` using `pathlib` (if it doesn't exist).
3. Create a log file named after the current date (`YYYY-MM-DD.log`).
4. Use `logging` to record:
   - program start,
   - successful log creation,
   - current user from environment variables (`os.environ`).
5. Check all existing log files in the folder:
   - if any are older than 3 days → delete them.
6. Print:
   - path to the current log file,
   - total number of log files remaining,
   - message `"=== DONE ==="`.

### Key Concepts
- `datetime.strftime()` and `strptime()` for date formatting and parsing  
- `logging` for recording events into files  
- `pathlib` for folder and file management  
- `os` for environment access and file deletion  

### Result
Each program run:
- writes logs into a file for the current day;
- automatically cleans logs older than 3 days;
- keeps the logs folder organized and up to date.