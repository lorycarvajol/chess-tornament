# models/tournament.py

from datetime import datetime


class Tournament:

    def __init__(self, name, location, date, players=None, is_finished=False):
        self.name = name
        self.location = location
        try:
            self.date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")
        self.players = players if players is not None else []
        self.is_finished = is_finished

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
