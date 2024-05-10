import json
import os
from models.tournament import Tournament


class TournamentController:
    """Contrôleur pour gérer les tournois."""

    def __init__(self, data_file="data/tournament_db.json"):
        """Initialiser le contrôleur avec le fichier JSON des tournois."""
        self.data_file = data_file
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        """Charger les tournois depuis un fichier JSON."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = file.read().strip()
                    if not data:
                        # Retourner une liste vide si le fichier est vide
                        return []
                    return [Tournament.from_dict(t) for t in json.loads(data)]
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error loading tournaments: {e}")
                return []
        return []

    def save_tournaments(self):
        """Sauvegarder tous les tournois dans un fichier JSON."""
        try:
            with open(self.data_file, "w") as file:
                json.dump([t.to_dict() for t in self.tournaments], file, indent=4)
        except IOError as e:
            print(f"Error saving tournaments: {e}")
