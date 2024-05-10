# models/match.py
class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None  # "player1", "player2", or "draw"

    def play_match(self):
        """Simule le résultat d'un match."""
        import random

        outcome = random.choice([0, 1, "draw"])
        if outcome == 0:
            self.result = f"{self.player1.first_name} wins"
            self.player1.update_score(1)
        elif outcome == 1:
            self.result = f"{self.player2.first_name} wins"
            self.player2.update_score(1)
        else:
            self.result = "Draw"
            self.player1.update_score(0.5)
            self.player2.update_score(0.5)

    def to_dict(self):
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "result": self.result,
        }

    def __repr__(self):
        return f"Match({self.player1.first_name} vs {self.player2.first_name}, Result: {self.result})"
