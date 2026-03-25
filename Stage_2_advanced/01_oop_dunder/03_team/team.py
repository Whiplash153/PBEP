class Team:
    def __init__(self, team, players):
        self.team = team
        self.players = players

    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return self.players[index]

    def __iter__(self):
        return iter(self.players)

    def __str__(self):
        return f"Team {self.team} with {len(self)} players"

    def __repr__(self):
        return f"Team(name='{self.team}', players='{self.players}'"

