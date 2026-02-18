employees = [
    {
        "name": "ivan",
        "stats": {
            "salary": 120000,
            "experience": 3
        },
        "active": True
    },
    {
        "name": "olga",
        "stats": {
            "salary": 90000,
            "experience": 5
        },
        "active": True
    },
    {
        "name": "petr",
        "stats": {
            "salary": 150000,
            "experience": 7
        },
        "active": False
    },
    {
        "name": "anna",
        "stats": {
            "salary": 70000,
            "experience": 1
        },
        "active": True
    },
]

filtered = []
for employee in employees:

    active = employee["active"]
    salary = employee["stats"]["salary"]
    exp = employee["stats"]["experience"]

    active_ok = active
    salary_ok = salary >= 100_000
    exp_ok = exp >= 3

    if active_ok and salary_ok and exp_ok:
        filtered.append(employee)

result = []
for employee in filtered:

    name = employee["name"]
    salary = employee["stats"]["salary"]
    exp = employee["stats"]["experience"]

    result.append({
        "employee": name.upper(),
        "level": "SENIOR" if exp >= 6 else "MIDDLE",
        "salary_k": salary / 1000
    })

print(result)
























