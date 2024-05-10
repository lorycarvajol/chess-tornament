class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None  # None, 1 (player1 wins), 2 (player2 wins), 0 (draw)

    def set_result(self, result):
        self.result = result
        if result == 1:
            self.player1.score += 1
        elif result == 2:
            self.player2.score += 1
        elif result == 0:
            self.player1.score += 0.5
            self.player2.score += 0.5

    def to_dict(self):
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "result": self.result,
        }
