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

    has_invalid_student = False

    for student in students:
        score = student["score"]
        if score < 80:
            has_invalid_student = True
            break

    if not has_invalid_student:
        name = course["title"]
        min_score = students[0]["score"]

        for student in students:
            score = student["score"]
            if score < min_score:
                min_score = score

        result.append({
            "course": name.upper(),
            "min_score": min_score
        })

print(result)





























