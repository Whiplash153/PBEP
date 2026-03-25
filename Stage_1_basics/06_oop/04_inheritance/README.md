# Task 4: Inheritance

**What I did**  
Created a base class `Person` and a subclass `Student` to learn inheritance.  
In practice, also made `Animal` and `Dog` classes to test how subclasses extend parent classes.  

**What I learned**  
- Inheritance allows one class (child) to reuse and extend functionality of another (parent).  
- `super().__init__()` calls the constructor of the parent to avoid code duplication.  
- Child classes can add new attributes and methods while keeping those of the parent.  
- Objects of child classes can use both parent methods and their own.  

**Practice**  
- In `demo.py`, tested `Person` and `Student`, confirmed that child inherits parent behavior.  
- In `task.py`, created `Animal` with `info()` and `Dog` with `bark()`; confirmed both parent and child methods work.