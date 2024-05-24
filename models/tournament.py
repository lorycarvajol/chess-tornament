# models/tournament.py
from datetime import datetime
from models.player import Player


class Tournament:
    def __init__(self, name, location, date, players=None, is_finished=False):
        self.name = name
        self.location = location
        try:
            self.date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")
        self.players = [
            Player.from_dict(p) if isinstance(p, dict) else p for p in (players or [])
        ]
        self.is_finished = is_finished

    def add_player(self, player):
        if isinstance(player, dict):
            player = Player.from_dict(player)
        self.players.append(player)

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
            "players": [player.to_dict() for player in self.players],
            "is_finished": self.is_finished,
        }

    @staticmethod
    def from_dict(data):
        return Tournament(
            name=data["name"],
            location=data["location"],
            date=data["date"],
            players=[Player.from_dict(p) for p in data.get("players", [])],
            is_finished=data.get("is_finished", False),
        )


def add_player(self, player):
    self.players.append(player)
