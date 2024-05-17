from datetime import datetime


class Tournament:

    def __init__(self, name, location, date, players=None, rounds=None):
        self.name = name
        self.location = location
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.players = players if players else []
        self.rounds = rounds if rounds else []

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
            "players": [player.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }
