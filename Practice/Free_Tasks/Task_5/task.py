employees = {
    "Ivan": 28,
    "Anna": 34,
    "Sergey": 41,
    "Masha": 25,
    "Oleg": 33
}

older_then_30 = [name for name, age in employees.items() if age > 30]
print("Names:", older_then_30)
print("Count:", len(older_then_30))