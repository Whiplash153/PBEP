class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

    def __str__(self):
        return f"Player {self.name} with {self.score} points"

    def __repr__(self):
        return f"Player(name='{self.name}', score={self.score})"

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score
