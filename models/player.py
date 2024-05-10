import re
from datetime import datetime


class Player:

    def __init__(
        self, first_name, last_name, date_of_birth, national_id, score=0, games_played=0
    ):
        # Utilisation de l'expression régulière pour inclure les lettres accentuées
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+$", first_name):
            raise ValueError(
                "Invalid first name. Please use alphabets and accented characters only."
            )
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+$", last_name):
            raise ValueError(
                "Invalid last name. Please use alphabets and accented characters only."
            )

        try:
            self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")

        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.score = score  # Total score in the tournament
        self.games_played = games_played  # Number of games played

    def __repr__(self):
        return f"Player({self.first_name} {self.last_name}, DOB: {self.date_of_birth.strftime('%d-%m-%Y')}, ID: {self.national_id}, Score: {self.score}, Games Played: {self.games_played})"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth.strftime("%d-%m-%Y"),
            "national_id": self.national_id,
            "score": self.score,
            "games_played": self.games_played,
        }

    def update_score(self, points):
        """Update the player's score and games played counters."""
        self.score += points
        self.games_played += 1
