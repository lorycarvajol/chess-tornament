import json
import os
from models.player import Player


class PlayerController:
    """Contrôleur pour la gestion des joueurs."""

    def __init__(self, data_file="data/players_db.json"):
        """Initialiser le contrôleur avec le fichier JSON des joueurs."""
        self.data_file = data_file
        self.players = self.load_players()

    def load_players(self):
        """Charger tous les joueurs depuis un fichier JSON."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    return [Player(**p) for p in data]
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error loading players: {e}")
                return []
        return []

    def save_players(self):
        """Sauvegarder tous les joueurs dans un fichier JSON."""
        try:
            with open(self.data_file, "w") as file:
                json.dump([p.to_dict() for p in self.players], file, indent=4)
        except IOError as e:
            print(f"Error saving players: {e}")

    def get_all_players(self):
        """Récupérer tous les joueurs chargés."""
        return self.players

    def add_player(self, first_name, last_name, date_of_birth, national_id):
        """Ajouter un joueur à la liste et sauvegarder les modifications."""
        if not all([first_name, last_name, date_of_birth, national_id]):
            print("All fields are required to add a player.")
            return
        new_player = Player(first_name, last_name, date_of_birth, national_id)
        self.players.append(new_player)
        self.save_players()

    def find_player(self, national_id):
        """Trouver un joueur par son identifiant national."""
        for player in self.players:
            if player.national_id == national_id:
                return player
        return None

    def update_player(self, national_id, **kwargs):
        """Mettre à jour les détails d'un joueur existant."""
        player = self.find_player(national_id)
        if player is not None:
            for key, value in kwargs.items():
                if hasattr(player, key):
                    setattr(player, key, value)
            self.save_players()
            return True
        print(f"Player with national_id {national_id} not found.")
        return False

    def remove_player(self, national_id):
        """Supprimer un joueur par son identifiant national."""
        initial_count = len(self.players)
        self.players = [p for p in self.players if p.national_id != national_id]
        if len(self.players) < initial_count:
            self.save_players()
            return True
        print(f"Player with national_id {national_id} not found.")
        return False
