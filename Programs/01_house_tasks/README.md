House Tasks Manager

This is a simple command-line program for managing household tasks.

What the program can do:
- add new tasks
- show the list of all tasks
- get a task by its ID
- save tasks between program runs

How to use

Run the file cli.py.

After start, you will see a menu with available actions.

1. Add task  
Adds a new task.  
The program will ask for:
- task title  
- responsible person  

Task ID is assigned automatically.

2. Tasks list  
Shows all tasks with their ID, status, title, and responsible person.

3. Get task by ID  
Allows you to enter a task ID and see details of that task.

4. Quit  
Exits the program.

Data storage

All tasks are stored in the file tasks.json.  
When the program starts, tasks are automatically loaded from this file.

Notes

- Task IDs are unique and do not depend on list order
- Data is preserved between program runs
- The program is designed to be used from the terminal