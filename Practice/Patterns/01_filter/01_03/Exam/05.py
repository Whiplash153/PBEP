courses = [
    {"title": "Python Basics",
     "info": {"year": 2020, "hours": 40},
     "students": [{"name": "bob", "score": 85}, {"name": "kate", "score": 92}]
    },

    {"title": "Data Science",
     "info": {"year": 2018, "hours": 60},
     "students": [{"name": "alice", "score": 95}, {"name": "mike", "score": 88}]
    },

    {"title": "Machine Learning",
     "info": {"year": 2022, "hours": 75},
     "students": [{"name": "john", "score": 90}, {"name": "anna", "score": 93}]
    },

    {"title": "Web Dev",
     "info": {"year": 2015, "hours": 30},
     "students": [{"name": "mark", "score": 70}, {"name": "sara", "score": 60}]
    },
]

filtered = []
for course in courses:

    year_ok = course["info"]["year"] >= 2020
    hours_ok = course["info"]["hours"] >= 40
    avg_ok = sum(student["score"] for student in course["students"]) / len(course["students"]) >= 90

    if year_ok and hours_ok and avg_ok:
        filtered.append(course)

result = []
for course in filtered:
    avg_score = sum(student["score"] for student in course["students"]) / len(course["students"])
    hours = course["info"]["hours"]

    if hours >= 70:
        difficulty = "HARD"
    elif hours >= 50:
        difficulty = "MEDIUM"
    else:
        difficulty = "EASY"

    result.append({
        "course": course["title"].upper(),
        "avg_score": round(avg_score),
        "difficulty": difficulty
    })

print(result)


