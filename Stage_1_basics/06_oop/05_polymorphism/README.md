# Task 5: Polymorphism

**What I did**  
Created a base class `Shape` with an abstract method `area()` and implemented subclasses (`Circle`, `Rectangle`) with their own versions.  
Also practiced with `Animal` subclasses (`Dog`, `Cat`) that override `sound()`.

**What I learned**  
- Polymorphism means the same method name can be used across different classes, but each class provides its own implementation.  
- Base classes can define a common interface (`area`, `sound`) that all children must follow.  
- With polymorphism, we can work with different objects in a single loop, calling the same method, and get different results.

**Practice**  
- In `demo.py`, called `.area()` on different shapes inside a loop.  
- In `task.py`, created a list of animals and each returned its own sound.