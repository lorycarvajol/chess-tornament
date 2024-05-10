from datetime import datetime


class Player:

    def __init__(self, first_name, last_name, date_of_birth, national_id):
        """Initialiser un joueur avec les détails donnés."""
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty.")

        self.first_name = first_name
        self.last_name = last_name

        # Valider le format de la date
        try:
            self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD-MM-YYYY.")

        # Valider l'identifiant national
        if not national_id:
            raise ValueError("National ID cannot be empty.")

        self.national_id = national_id

    def to_dict(self):
        """Convertir l'objet Player en dictionnaire pour la sérialisation JSON."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth.strftime("%d-%m-%Y"),
            "national_id": self.national_id,
        }

    @staticmethod
    def from_dict(data):
        """Créer un objet Player à partir d'un dictionnaire."""
        return Player(
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
            national_id=data["national_id"],
        )

    def __repr__(self):
        """Afficher une représentation lisible de l'objet Player."""
        return f"<Player: {self.first_name} {self.last_name}, DOB: {self.date_of_birth}, ID: {self.national_id}>"
