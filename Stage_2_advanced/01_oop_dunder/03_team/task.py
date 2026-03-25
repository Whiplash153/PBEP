from team import Team

team = Team ("Rangers", ["Harry", "Howard", "Willis", "Tug"])

print(team)

print(len(team))

print(team[0], team[-1])

for player in team:
    print(player)