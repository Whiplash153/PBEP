from player import Player

p1 = Player("Alice", "100")
p2 = Player("Bob", "150")
p3 = Player("Charlie", "100")

print(p1)
print(repr(p2))

print(p1 == p3)
print(p1 < p2)
print(p2 > p3)