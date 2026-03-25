# Contact Manager (Case)

## What this program does
This case demonstrates how basic Python data structures (list, dict, set, tuple) can be combined into a practical tool.  
The program is a simple **console contact manager**: it allows the user to add contacts, show them, search, delete, and view statistics.

## Why it is useful
Keeping track of contacts is a very common real-world task. Even in its simplest form, such an app shows the value of combining fundamental programming tools into something meaningful. It connects directly to everyday needs like storing phone numbers or managing a small contact book.

## What is inside
- **Data model**:  
  - Each contact is a dictionary with two fields: `name` and `phone`.  
  - All contacts are stored in a list.  
  - A set (`names_index`) keeps track of unique names for fast lookup.
- **Functions**:  
  - `add_contact()` — add a new contact (checks duplicates).  
  - `show_all_contacts()` — show all stored contacts.  
  - `find_contact()` — search by name (case-insensitive).  
  - `delete_contact()` — delete a contact by name.  
  - `show_stats()` — display total number of contacts and unique names.
- **Menu loop**:  
  Simple text interface with options (1–5, 0 to exit). The menu repeats until the user exits.

## Tools and concepts used
- Lists, dictionaries, and sets working together.  
- Functions with clear responsibilities.  
- Input/output with the user.  
- Control flow (loops, conditions).  
- Basic error handling with checks for duplicates, empty input, or missing contacts.

## What I learned
- How to combine different structures into one coherent program.  
- How to separate logic into functions and keep code readable.  
- How indexing and uniqueness (set) can make operations more reliable.  
- How a simple menu-driven loop can turn small pieces of logic into a usable application.