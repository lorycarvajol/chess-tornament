# models/tournament_session.py
from datetime import datetime


class TournamentSession:
    def __init__(self, tournament, players):
        self.tournament = tournament
        self.players = players
        self.start_date = datetime.now()
        self.matches = []  # Cette liste pourrait être utilisée pour suivre les matches
        self.is_active = True

    def add_match_result(self, player1, player2, winner):
        match = {
            "player1": player1,
            "player2": player2,
            "winner": winner,
            "date": datetime.now(),
        }
        self.matches.append(match)

    def end_tournament(self):
        self.is_active = False

    def to_dict(self):
        return {
            "tournament": self.tournament.to_dict(),
            "players": [player.to_dict() for player in self.players],
            "start_date": self.start_date.strftime("%d-%m-%Y %H:%M:%S"),
            "matches": self.matches,
            "is_active": self.is_active,
        }
