# OS (Standard Library)

## Goal
Learn to work with the operating system using Python’s built-in `os` module.

## Overview
This task covers how to manage files, folders, and environment variables at a system level.

### Step 1 — Overview
- Explored basic commands: `os.name`, `os.getcwd()`, `os.listdir()`, `os.mkdir()`, and `os.rmdir()`.

### Step 2 — Navigation
- Learned to move between directories with `os.chdir()`.
- Created nested folders using `os.makedirs()`.
- Worked with paths using `os.path.join()`.

### Step 3 — Environment Variables
- Accessed environment variables through `os.environ`.
- Read system variables like `USER`, `HOME`, and `PATH`.
- Added and deleted temporary variables within the Python session.

### Step 4 — Mini Practice
- Created a folder `system_test`.
- Switched into it and created a file `test.txt` containing the current user.
- Printed the current directory.
- Returned to the original directory.
- Deleted the created file and folder.
- Displayed part of the system `PATH`.

## Key Concepts
- `os.getcwd()` / `os.chdir()` — current directory management  
- `os.mkdir()` / `os.rmdir()` — folder creation and deletion  
- `os.listdir()` — directory contents  
- `os.path.join()` — safe path building  
- `os.environ` — access to environment variables  