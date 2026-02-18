projects = [
    {"title": "alpha",  "team": 6,  "budget": 1_200_000, "duration": 14, "rating": 4.6},
    {"title": "beta",   "team": 12, "budget": 3_500_000, "duration": 30, "rating": 4.1},
    {"title": "gamma",  "team": 8,  "budget": 900_000,   "duration": 10, "rating": 4.8},
    {"title": "delta",  "team": 15, "budget": 7_000_000, "duration": 45, "rating": 4.3},
    {"title": "epsilon","team": 3,  "budget": 400_000,   "duration": 6,  "rating": 4.9},
]

filtered = []
for project in projects:

    team = project["team"]
    budget = project["budget"]
    duration = project["duration"]
    rating = project["rating"]

    team_ok = team >= 6
    budget_ok = budget >= 1_000_000
    duration_ok = duration >= 12
    rating_ok = rating >= 4.5

    if team_ok and budget_ok and duration_ok and rating_ok:
        filtered.append(project)

result = []
for project in filtered:

    team = project["team"]
    budget = project["budget"]
    duration = project["duration"]
    rating = project["rating"]

    if rating >= 4.8:
        category = "A"
    elif rating >= 4.5:
        category = "B"
    else:
        category = "C"

    result.append({
        "project": project["title"].upper(),
        "efficiency": budget / duration,
        "category": category
    })

print(result)
