students = [
    {"name": "bob",   "math": 90, "english": 70, "passed": True},
    {"name": "alice", "math": 65, "english": 85, "passed": True},
    {"name": "mike",  "math": 40, "english": 55, "passed": False},
    {"name": "kate",  "math": 95, "english": 95, "passed": True},
    {"name": "john",  "math": 50, "english": 45, "passed": False},
]

filtered = []
for student in students:
    if student["passed"] and student["math"] >= 80 and student["english"] >= 80:
        filtered.append(student)

result = []
for student in filtered:
    result.append({
        "student": student["name"].upper(),
        "avg_score": (student["math"] + student["english"]) / 2,
        "status": "EXCELLENT"
    })

print("Result:", result)