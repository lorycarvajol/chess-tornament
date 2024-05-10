import random


class Round:

    def __init__(self, round_number, matches=[]):
        self.round_number = round_number
        self.matches = matches

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [match.to_dict() for match in self.matches],
        }
