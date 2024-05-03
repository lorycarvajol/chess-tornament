import re
from datetime import datetime


class Player:
    def __init__(self, first_name, last_name, date_of_birth, national_id):
        if not re.match("^[A-Za-z]+$", first_name):
            raise ValueError("Invalid first name. Please use alphabets only.")
        if not re.match("^[A-Za-z]+$", last_name):
            raise ValueError("Invalid last name. Please use alphabets only.")
        try:
            # This ensures the date is not only valid format but also a logical date
            self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")

        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id

    def __repr__(self):
        return f"Player({self.first_name} {self.last_name}, DOB: {self.date_of_birth}, ID: {self.national_id})"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth.strftime("%d-%m-%Y"),
            "national_id": self.national_id,
        }
