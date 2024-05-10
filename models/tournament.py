from datetime import datetime
from models.player import Player
from models.round import Round
from models.match import Match


class Tournament:

    def __init__(self, name, location, date, players=None, rounds=None):
        self.name = name
        self.location = location
        self.date = (
            datetime.strptime(date, "%d-%m-%Y") if isinstance(date, str) else date
        )
        self.players = [
            Player(**player) for player in (players or [])
        ]  # Créer des objets Player
        self.rounds = [
            Round(**round) for round in (rounds or [])
        ]  # Créer des objets Round

    def add_player(self, player):
        self.players.append(player)

    def create_round(self):
        sorted_players = sorted(self.players, key=lambda x: x.score, reverse=True)
        matches = []
        for i in range(0, len(sorted_players) - 1, 2):
            match = Match(sorted_players[i], sorted_players[i + 1])
            matches.append(match)
        new_round = Round(len(self.rounds) + 1, matches)
        self.rounds.append(new_round)
        return new_round

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
            "players": [player.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }
