# Team with Collection Protocols

We created a `Team` class that behaves like a collection.

## Implemented dunder methods
- `__len__` → allows calling `len(team)` to get the number of players.
- `__getitem__` → allows indexing: `team[0]`, `team[-1]`.
- `__iter__` → allows iterating with a `for` loop.
- `__str__` → human-friendly string when printing.
- `__repr__` → debug representation of the object.

## Example
```python
from team import Team

team = Team("Rangers", ["Harry", "Howard", "Willis", "Tug"])

print(team)            # Team Rangers with 4 players
print(len(team))       # 4
print(team[0])         # Harry
print(team[-1])        # Tug

for player in team:
    print(player)

# Output:
# Team Rangers with 4 players
# 4
# Harry
# Tug
# Harry
# Howard
# Willis
# Tug
```