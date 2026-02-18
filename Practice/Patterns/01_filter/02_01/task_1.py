employees = [
    {"name": "alex", "age": 31, "dept": "it",     "salary": 120000, "years": 5},
    {"name": "mike", "age": 28, "dept": "hr",     "salary": 70000,  "years": 2},
    {"name": "kate", "age": 35, "dept": "it",     "salary": 150000, "years": 7},
    {"name": "olga", "age": 26, "dept": "design", "salary": 65000,  "years": 1},
    {"name": "ivan", "age": 42, "dept": "it",     "salary": 200000, "years": 10},
]

filtered = []
for employee in employees:

    age_ok = employee["age"] >= 30
    years_ok = employee["years"] >= 5
    dept_ok = employee["dept"] == "it"
    salary_ok = employee["salary"] >= 130000

    if years_ok and dept_ok and salary_ok and age_ok:
        filtered.append(employee)

result = []
for employee in filtered:

    if employee["years"] >= 7:
        level = "senior"
    elif employee["years"] >= 3:
        level = "middle"
    else:
        level = "junior"

    result.append({
        "employee": employee["name"].upper(),
        "total_income": employee["salary"] * 12,
        "level": level
    })

print(result)

