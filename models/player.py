import json


class Player:
    def __init__(self, first_name, last_name, birthdate, player_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.id = player_id

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birthdate=data["birthdate"],
            player_id=data.get("id"),
        )
