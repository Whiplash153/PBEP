from shapes import Shape, Circle, Rectangle

shapes = [
    Circle(5),
    Rectangle(4, 4),
    Circle(10)
]

for shape in shapes:
    print(f"Area: {shape.area()}")

