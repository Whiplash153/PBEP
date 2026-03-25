# Working with Sets

In this task we practiced the basics of Python sets (unique collections of elements).

## What we covered
- Creating sets and understanding that duplicates are automatically removed.
- Checking membership with `in`.
- Adding elements with `.add()`.
- Removing elements:
  - `.discard()` (safe, no error if not found),
  - `.remove()` (raises an error if element is missing),
  - `.pop()` (removes and returns a random element),
  - `.clear()` (empties the set).
- Set operations:
  - Union (`|`) — combine all elements without duplicates,
  - Intersection (`&`) — elements common to both sets,
  - Difference (`-`) — elements in one set but not the other,
  - Symmetric difference (`^`) — elements in either set but not in both.
- Using sets to remove duplicates from lists (via `set()` and then converting back to `list()`).
- Mini-case: comparing registered vs active users to find inactive, ghost, and loyal users.

## Practical task
Create a set with three friends.  
1. Add one more friend.  
2. Remove one friend.  
3. Check if `"Alex"` is in the set.  
4. Print the final set.

## Conclusion
Sets are a powerful data structure when working with collections of unique elements.  
They are especially useful for membership tests, removing duplicates, and comparing groups of data.