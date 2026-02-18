# Pathlib (Standard Library)

## Goal
Learn how to use Python's `pathlib` module to work with files and directories in an object-oriented, cross-platform way.

## Overview
This task covered all the main features of `pathlib` — from working with paths to creating, reading, traversing, and deleting files and folders.

### Step 1 — Working with Paths
- Used `Path.cwd()` to get the current directory.
- Combined paths using the `/` operator.
- Checked existence and type of files/folders with `.exists()`, `.is_file()`, and `.is_dir()`.

### Step 2 — Working with Files
- Created and wrote to files using `.write_text()`.
- Read content with `.read_text()`.
- Understood that files are automatically created and closed safely by `pathlib`.

### Step 3 — Traversing Directories
- Iterated through directories using `.iterdir()`.
- Filtered files by extension with `.glob("*.py")`.
- Used `.rglob()` for recursive search across subdirectories.

### Step 4 — Creating and Deleting
- Created folders with `.mkdir(exist_ok=True)`.
- Deleted files safely using `.unlink()` and folders using `.rmdir()`.
- Implemented existence checks before deletion to avoid errors.

### Mini Practice
- Created a `project_data` folder.
- Added three text files: `notes.txt`, `report.txt`, and `summary.txt`.
- Listed all `.txt` files and counted them.
- Deleted all files and the folder afterwards.
- Result: full control over the filesystem via `pathlib`.

## Key Concepts
- `Path` objects as modern replacements for `os.path`
- File operations: `.write_text()`, `.read_text()`, `.unlink()`
- Folder operations: `.mkdir()`, `.rmdir()`
- Iterating and filtering: `.iterdir()`, `.glob()`, `.rglob()`
- Safe existence checks with `.exists()`