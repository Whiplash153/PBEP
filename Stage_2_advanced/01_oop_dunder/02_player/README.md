# Player with Comparison

We created a `Player` class with several dunder methods:

- `__init__`: sets name and score.  
- `__str__`: returns a human-friendly string, e.g. `Player Dave with 200 points`.  
- `__repr__`: returns a debug representation, e.g. `Player(name='Dave', score=200)`.  
- `__eq__`: checks if two players have the same score.  
- `__lt__`: checks if one player has fewer points.  
- `__gt__`: checks if one player has more points.  

This allows us to compare players directly (`>`, `<`, `==`) and see meaningful output in `print()` or in debug.