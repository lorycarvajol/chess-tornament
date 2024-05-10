import json
from models.player import Player


class Tournament:

    def __init__(self, name, location, date, players):
        self.name = name
        self.location = location
        self.date = date
        self.players = players

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "players": [player.to_dict() for player in self.players],
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            location=data["location"],
            date=data["date"],
            players=[Player.from_dict(p) for p in data["players"]],
        )

    def save(self, file_path):
        with open(file_path, "w") as file:
            json.dump(self.to_dict(), file)
