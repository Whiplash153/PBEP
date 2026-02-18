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

    has_flop_students = False
    for student in students:
        if student["score"] < 80:
            has_flop_students = True
            break

    if not has_flop_students:

        total_score = 0
        count = 0

        for student in students:
            total_score += student["score"]
            count += 1

        avg_score = total_score / count

        result.append({
            "course": course["title"].upper(),
            "avg_score": avg_score
        })

print(result)
