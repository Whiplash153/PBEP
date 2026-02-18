class Player:
    def __init__(self, player, score):
        self.player = player
        self.score = int(score)

    def __str__(self):
        return f"Player {self.player} with {self.score} points"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Player(self.player, self.score + other)
        elif isinstance(other, Player):
            return Player(self.player, self.score + other.score)
        else:
            raise TypeError("Can only add int, float or Player to Player")


player1 = Player("Dave", 30)

print(player1)
print(player1 + 2)