# Task: Students' Task Completion Stats

## Condition
Each student has a name and a number of completed assignments.  
You need to display the names of all students who completed more than 5 tasks and calculate the average number of tasks in the group.

## Solution
We stored the students' names and completed task counts in a dictionary.  
Then used a **list comprehension** to filter students with more than 5 completed tasks.  
Next, we iterated over the dictionary using `.items()` to calculate the total and derived the average by dividing by the number of students.

**Tools used:** dict, list comprehension, for-loop, len(), print.