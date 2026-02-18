employees = [
    {"name": "bob",    "salary": 3000, "hours": 160, "remote": False},
    {"name": "alice",  "salary": 4500, "hours": 150, "remote": True},
    {"name": "mike",   "salary": 2200, "hours": 170, "remote": False},
    {"name": "kate",   "salary": 5200, "hours": 155, "remote": True},
    {"name": "john",   "salary": 2800, "hours": 180, "remote": False},
]

filtered = []
for emp in employees:
    if (
        emp["salary"] >= 3000
        and emp["hours"] <= 160
        and (emp["remote"] or emp["salary"] >= 5000)
    ):
        filtered.append(emp)

result = []
for emp in filtered:

    if emp["remote"] and emp["salary"] >= 5000:
        bonus = 700
    elif emp["remote"]:
        bonus = 200
    elif emp["salary"] >= 5000:
        bonus = 500
    else:
        bonus = 0

    adjusted_salary = emp["salary"] + bonus

    result.append({
        "employee": emp["name"].upper(),
        "adjusted_salary": adjusted_salary,
        "class": "A" if adjusted_salary >= 5000 else "B"
    })

print(result)