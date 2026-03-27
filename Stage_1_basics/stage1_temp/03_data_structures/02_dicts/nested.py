player = {
    "name": "LeBron James",
    "team": "Lakers",
    "stats": {
        "points": 28,
        "assists": 8
    }
}

name = player["name"]
pts = player["stats"]["points"]

player["stats"]["assists"] = 9

player["stats"]["rebounds"] = 7

steals = player["stats"].get("steals")
steals_def = player["stats"].get("steals", 0)

print(name, player["stats"]["assists"])

def update_stats(player, points=0, assists=0, rebounds=0):
    player["stats"]["points"] += points
    player["stats"]["assists"] += assists
    player["stats"]["rebounds"] = player["stats"].get("rebounds", 0) + rebounds
    return player

updated = update_stats(player, points=12, assists=3, rebounds=5)
print(updated)