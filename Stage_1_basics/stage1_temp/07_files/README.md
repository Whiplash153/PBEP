# Files

In this topic we learned how to work with files in Python.

## Tools
- `open("file.txt", "w")` — write mode, creates or overwrites a file.
- `open("file.txt", "a")` — append mode, adds new data at the end.
- `open("file.txt", "r")` — read mode, opens file for reading.
- `with open(...) as f:` — safe way to open and automatically close files.
- `f.write("text")` — write text to file.
- `f.read()` — read whole file.
- `f.readlines()` — read file into list of lines.
- Loop `for line in f:` — read file line by line.

## Case: Notes
We built a simple program where you can:
- add notes (`add_note(text)`);
- read all notes (`show_notes()`).

Every run starts with an empty `notes.txt` file.  
Example output:
```
All notes:
First note
Second note
```

## Result
Now we can create, read, and update text files. This is the base for logs, configs, and saving user data.