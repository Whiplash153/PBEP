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

filtered = []

for course in courses:
    students = course["students"]

    has_top_student = False

    for student in students:
        if student["score"] >= 90:
            has_top_student = True
            break

    if has_top_student:

        top_students = []

        for student in students:
            if student["score"] >= 90:
                top_students.append(student["name"])

        filtered.append({
            "course": course["title"].upper(),
            "top_students": top_students
        })

print(filtered)
