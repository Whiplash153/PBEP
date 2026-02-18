# Working with Dictionaries

In this task we practiced the basics of Python dictionaries (key–value storage).

## What we covered
- Creating dictionaries with key–value pairs.
- Accessing values by key (`dict[key]`).
- Safe access with `.get()`, including default values.
- Checking if a key exists with `in`.
- Adding new pairs and updating existing ones.
- Using `.update()` to modify multiple keys at once.
- Removing elements with `del`, `.pop()`, `.popitem()`, and `.clear()`.
- Iterating over dictionaries:
  - keys (`for key in dict`);
  - values (`for value in dict.values()`);
  - pairs (`for key, value in dict.items()`).
- Nested dictionaries and updating values inside them.
- Mini-case: updating a player's stats through a function (`update_stats`).

## Practical task
Create a dictionary with book information (`title`, `author`, `year`).  
1. Print the title.  
2. Add the `pages` key.  
3. Update the year.  
4. Remove the author.  
5. Print the final dictionary.  

## Conclusion
Dictionaries are one of the core data structures in Python.  
They are useful for storing structured information, such as user profiles, configuration, or JSON data.  
We learned how to create, update, delete, and iterate over them, as well as how to handle nested dictionaries safely.