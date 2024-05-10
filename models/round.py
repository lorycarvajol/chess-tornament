# models/round.py
class Round:

    def __init__(self, number, matches):
        self.number = number
        self.matches = matches

    def play_round(self):
        """Simule le résultat de chaque match dans cette ronde."""
        for match in self.matches:
            match.play_match()

    def to_dict(self):
        return {
            "number": self.number,
            "matches": [match.to_dict() for match in self.matches],
        }

    def __repr__(self):
        return f"Round({self.number}, Matches: {len(self.matches)})"
