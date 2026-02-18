# Task: Player Score Addition

## Condition
Create a class `Player` that stores a player's name and score.  
Implement string representation and the ability to add points to a player using the `+` operator.  
The addition should return a **new Player object**, not modify the original one.

## Solution
We implemented the `Player` class with the following methods:
- `__init__` — initializes a player with `name` and `score`.
- `__str__` — returns a readable description of the player.
- `__add__` — overloads the `+` operator to allow:
  - adding an integer or float to the player's score;
  - adding scores of two `Player` objects;
  - raising a `TypeError` for invalid operand types.

**Tools used:** class, attributes, dunder methods (`__init__`, `__str__`, `__add__`), type checking.