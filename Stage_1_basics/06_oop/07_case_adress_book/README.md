# Case: Address Book

**What I did**  
- Implemented a simple address book with two classes:  
  - `Contact` (stores name and phone, has `__str__` for readable output).  
  - `AddressBook` (stores a list of contacts, with methods to add, find, and show all).  
- Wrote a demo scenario in `app.py` to show how it works.

**What I learned**  
- How to combine OOP basics (classes, methods, dunder methods) into a single mini-application.  
- Encapsulation: the `AddressBook` keeps its own list of contacts and exposes only methods to work with it.  
- Polymorphism with `__str__`: all `Contact` objects print nicely in loops.  
- How to build a small but functional program step by step.

**Run result**
```
Found: Bob: 67890

All contacts
Anna: 12345
Bob: 67890
Kate: 54321
```