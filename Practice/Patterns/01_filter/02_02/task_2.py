projects = [
    {
        "title": "alpha",
        "meta": {
            "budget": 1_200_000,
            "duration": 14
        },
        "team": {
            "size": 6,
            "remote": True
        }
    },
    {
        "title": "beta",
        "meta": {
            "budget": 700_000,
            "duration": 10
        },
        "team": {
            "size": 4,
            "remote": False
        }
    },
    {
        "title": "gamma",
        "meta": {
            "budget": 3_500_000,
            "duration": 30
        },
        "team": {
            "size": 12,
            "remote": True
        }
    },
    {
        "title": "delta",
        "meta": {
            "budget": 900_000,
            "duration": 20
        },
        "team": {
            "size": 8,
            "remote": True
        }
    },
]

filtered = []
for project in projects:

    budget = project["meta"]["budget"]
    duration = project["meta"]["duration"]
    size = project["team"]["size"]
    remote = project["team"]["remote"]

    budget_ok = budget >= 1_000_000
    duration_ok = duration >= 14
    size_ok = size >= 6
    remote_ok = remote

    if budget_ok and duration_ok and size_ok and remote_ok:
        filtered.append(project)

result = []
for project in filtered:

    title = project["title"]
    budget = project["meta"]["budget"]
    duration = project["meta"]["duration"]
    remote = project["team"]["remote"]

    result.append({
        "project": title.upper(),
        "cost_per_day": budget / duration,
        "team_type": "REMOTE" if remote else "OFFICE"
    })

print(result)


































