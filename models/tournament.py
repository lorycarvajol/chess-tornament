import re
from datetime import datetime


class Tournament:

    def __init__(self, name, location, date):
        if not re.match("^[A-Za-z0-9\s]+$", name):
            raise ValueError(
                "Invalid tournament name. Please use alphanumeric characters and spaces only."
            )
        if not re.match("^[A-Za-z0-9\s,]+$", location):
            raise ValueError(
                "Invalid location. Please use alphanumeric characters, commas, and spaces only."
            )
        try:
            # This ensures the date is not only valid format but also a logical date
            self.date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")

        self.name = name
        self.location = location

    def __repr__(self):
        return f"Tournament(Name: {self.name}, Location: {self.location}, Date: {self.date.strftime('%d-%m-%Y')})"

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
        }
