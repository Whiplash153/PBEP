users = [
    {"username": "bob",   "profile": {"age": 25, "active": True},  "scores": [100, 95, 88]},
    {"username": "alice", "profile": {"age": 17, "active": True},  "scores": [80, 70, 60]},
    {"username": "mike",  "profile": {"age": 30, "active": False}, "scores": [90, 85, 100]},
    {"username": "kate",  "profile": {"age": 22, "active": True},  "scores": [95, 98, 99]},
]

filtered = []
for user in users:

    age_ok = user["profile"]["age"] >= 18
    profile_ok = user["profile"]["active"]
    avg_ok = (sum(user["scores"]) / len(user["scores"])) >= 90

    if age_ok and profile_ok and avg_ok:
        filtered.append(user)

result = []
for user in filtered:
    avg_score = sum(user["scores"]) / len(user["scores"])

    result.append({
        "user": user["username"].upper(),
        "avg_score": round(avg_score),
        "status": "TOP" if avg_score >= 95 else "GOOD"
    })

print(result)