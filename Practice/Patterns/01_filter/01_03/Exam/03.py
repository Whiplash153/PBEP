players = [
    {"name": "alex",  "stats": {"wins": 15, "losses": 3},  "scores": [98, 95, 92]},
    {"name": "bob",   "stats": {"wins": 8,  "losses": 10}, "scores": [70, 75, 80]},
    {"name": "kate",  "stats": {"wins": 20, "losses": 2},  "scores": [100, 99, 97]},
    {"name": "mike",  "stats": {"wins": 12, "losses": 6},  "scores": [85, 88, 90]},
]

filtered = []
for player in players:

    wins_ok = player["stats"]["wins"] >= 10
    diff_ok = player["stats"]["wins"] - player["stats"]["losses"] >= 5
    avg_ok = sum(player["scores"]) / len(player["scores"]) >= 90

    if wins_ok and diff_ok and avg_ok:
        filtered.append(player)

result = []
for player in filtered:
    round_avg = round(sum(player["scores"]) / len(player["scores"]))

    if round_avg >= 97:
        rank = "S"
    elif round_avg >= 93:
        rank = "A"
    else:
        rank = "B"

    result.append({
        "player": player["name"].upper(),
        "rating": round_avg,
        "rank": rank
    })

print(result)