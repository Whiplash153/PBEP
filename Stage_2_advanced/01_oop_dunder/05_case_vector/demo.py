from vector import Vector

a = Vector(2, 3)
b = Vector(4, 1)

print(a)
print(b)

print("a + b =", a + b)
print("a == b:", a == b)

for value in a:
    print("Element:", value)

print("Length of a:", len(a))
