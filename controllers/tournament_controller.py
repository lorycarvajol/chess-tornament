import json
import os


class TournamentController:
    def __init__(self, file_path):
        """
        Initialise le contrôleur de tournoi avec le chemin du fichier de données.

        Args:
            file_path (str): Chemin vers le fichier JSON où les données des tournois sont stockées.
        """
        self.file_path = file_path
        self.ensure_file_exists()
        print(
            f"TournamentController initialisé avec le fichier de données : {file_path}"
        )

    def ensure_file_exists(self):
        """
        Vérifie si le fichier de données existe et s'il est vide, il crée un fichier vide.
        """
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            with open(self.file_path, "w") as f:
                json.dump([], f)
            print(f"Fichier de données créé à : {self.file_path}")

    def load_data(self):
        """
        Charge les données du fichier JSON.

        Returns:
            list: Une liste des tournois chargés depuis le fichier.
        """
        with open(self.file_path, "r") as f:
            try:
                data = json.load(f)
                print("Données chargées avec succès.")
                return data
            except json.JSONDecodeError:
                print(
                    "Erreur lors du chargement des données. Le fichier JSON est peut-être corrompu."
                )
                return []

    def save_data(self, data):
        """
        Sauvegarde les données dans le fichier JSON.

        Args:
            data (list): Les données des tournois à sauvegarder.
        """
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
        print("Données sauvegardées avec succès.")

    def add_tournament(self, name, location, date):
        """
        Ajoute un nouveau tournoi aux données existantes.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            date (str): Date du tournoi (format DD-MM-YYYY).
        """
        data = self.load_data()
        new_id = max([t["id"] for t in data], default=0) + 1
        new_tournament = {
            "id": new_id,
            "name": name,
            "location": location,
            "date": date,
            "is_finished": False,
        }
        data.append(new_tournament)
        self.save_data(data)
        print(f"Tournoi '{name}' ajouté avec succès (ID: {new_id}).")

    def list_tournaments(self):
        """
        Liste tous les tournois enregistrés.

        Returns:
            list: Une liste des tournois.
        """
        tournaments = self.load_data()
        if tournaments:
            print("Liste des tournois :")
            for tournament in tournaments:
                print(
                    f"ID: {tournament['id']}, Nom: {tournament['name']}, Lieu: {tournament['location']}, Date: {tournament['date']}"
                )
        else:
            print("Aucun tournoi trouvé.")
        return tournaments
