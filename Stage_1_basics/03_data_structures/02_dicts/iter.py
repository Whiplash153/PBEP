player = {
    "name": "LeBron James",
    "team": "Lakers",
    "points": 28,
    "assists": 8
}

for key in player:
    print("key:", key)

for value in player.values():
    print("value:", value)

for key, value in player.items():
    print(f"{key} -> {value}")
