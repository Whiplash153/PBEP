# 	ВСЕ → проверка < порога + флаг + break
# 	ХОТЯ БЫ ОДИН → проверка >= порога + флаг + break
# 	ХОТЯ БЫ N → ТОЛЬКО СЧЁТЧИК, без флага

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

        top_count = 0

        for student in students:
            if student["score"] >= 90:
                top_count += 1

        filtered.append({
            "course": course["title"].upper(),
            "top_count": top_count
        })

print(filtered)