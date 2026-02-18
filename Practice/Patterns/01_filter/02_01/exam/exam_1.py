users = [
    {"name": "alice", "age": 22, "active": True},
    {"name": "bob", "age": 17, "active": True},
    {"name": "carol", "age": 35, "active": False},
    {"name": "dave", "age": 28, "active": True},
]

filtered = []
for user in users:

    age = user["age"]
    active = user["active"]

    age_ok = age >= 21
    active_ok = active

    if age_ok and active_ok:
        filtered.append(user)

result = []
for user in filtered:

    user_name = user["name"]
    user_age = user["age"]

    result.append({
        "user": user_name.upper(),
        "age_group": "young" if user_age < 30 else "adult"
    })

print(result)
