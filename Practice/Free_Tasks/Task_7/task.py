students = {
    "Ivan": 3,
    "Anna": 8,
    "Sergey": 5,
    "Masha": 9,
    "Oleg": 2
}

did_the_task = [name for name, score in students.items() if score > 5]
print(did_the_task)

total = 0
for name, score in students.items():
        total += score

print("Final:", total / len(students))
