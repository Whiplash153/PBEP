from team import Team

team = Team("Warriors", ["Alice", "Bob", "Charlie"])

print(team)

print(len(team))

print(team[0])

for player in team:
    print(player)