player = {
    "name": "LeBron James",
    "team": "Lakers",
    "points": 28
}

name = player["name"]

assists = player.get("assists")
assists_with_default = player.get("assists", 0)

has_team = "team" in player

