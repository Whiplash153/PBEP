employees = [
    {"name": "ivan", "salary": 120000, "experience": 3},
    {"name": "olga", "salary": 90000,  "experience": 5},
    {"name": "petr", "salary": 150000, "experience": 7},
    {"name": "anna", "salary": 70000,  "experience": 1},
]

filtered = []
for employee in employees:

    salary = employee["salary"]
    experience = employee["experience"]

    salary_ok = salary >= 100000
    experience_ok = experience >= 3

    if salary_ok and experience_ok:
        filtered.append(employee)

result = []
for employee in filtered:

    name = employee["name"]
    salary = employee["salary"]
    experience = employee["experience"]

    result.append({
        "employee": name.upper(),
        "grade": "SENIOR" if experience >= 6 else "MIDDLE",
        "salary_k": round(salary / 1000)
    })

print(result)
