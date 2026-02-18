courses = [
    {
        "title": "python",
        "students": [
            {"name": "alice", "score": 82},
            {"name": "bob", "score": 91},
        ]
    },
    {
        "title": "math",
        "students": [
            {"name": "carol", "score": 77},
        ]
    },
    {
        "title": "physics",
        "students": [
            {"name": "dave", "score": 95},
            {"name": "eva", "score": 93},
        ]
    }
]

result = []

for course in courses:
    students = course["students"]

    count_1 = 0
    for student in students:
        if student["score"] >= 90:
            count_1 += 1

    if count_1 >= 2:

        result.append({
            "course": name.upper(),
            "top_count": count
        })

print(result)