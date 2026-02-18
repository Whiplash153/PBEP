employees = [
    {"name": "bob", "salary": 90000, "department": "it"},
    {"name": "alice", "salary": 120000, "department": "hr"},
    {"name": "mike", "salary": 150000, "department": "it"},
    {"name": "kate", "salary": 70000, "department": "sales"},
    {"name": "john", "salary": 110000, "department": "it"},
]

filtered = []
for emp in employees:
    if emp["department"] == "it" and emp["salary"] > 100000:
        filtered.append(emp)

result = []
for item in filtered:
    result.append({
        "employee": item["name"].upper(),
        "income": round(item["salary"] * 1.15)
    })

print("Result:", result)