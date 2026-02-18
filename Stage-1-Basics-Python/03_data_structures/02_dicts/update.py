player = {
    "name": "LeBron James",
    "team": "Lakers",
    "points": 28
}

player ["assists"] = 8

player ["points"] = 30

player.update({"rebounds": 7, "team": "Cavs"})

del player["rebounds"]

points = player.pop("points")

last_item = player.popitem()

player.clear()