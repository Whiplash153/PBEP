users = [
    {
        "profile": {"name": "alice", "age": 25},
        "settings": {"active": True}
    },
    {
        "profile": {"name": "bob", "age": 19},
        "settings": {"active": True}
    },
    {
        "profile": {"name": "carol", "age": 32},
        "settings": {"active": False}
    },
    {
        "profile": {"name": "dave", "age": 40},
        "settings": {"active": True}
    },
]

filtered = []
for user in users:

    age = user["profile"]["age"]
    active = user["settings"]["active"]

    age_ok = age >= 21
    active_ok = active

    if age_ok and active_ok:
        filtered.append(user)

result = []
for user in filtered:

    name = user["profile"]["name"]
    age = user["profile"]["age"]

    result.append({
        "user": name.upper(),
        "group": "adult" if age >= 30 else "young"
    })

print(result)


