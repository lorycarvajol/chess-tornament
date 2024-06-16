import os
import json
from models.tournament_round import TournamentRoundModel


class TournamentSessionController:
    def __init__(self, data_path):
        """
        Initialise le contrôleur de session de tournoi avec le chemin des données.

        Args:
            data_path (str): Chemin vers le dossier contenant les données des sessions de tournoi.
        """
        self.data_path = data_path
        self.sessions_file = os.path.join(self.data_path, "tournament_sessions.json")
        self.round_model = TournamentRoundModel(self.data_path)
        self.ensure_sessions_file()
        print(
            f"TournamentSessionController initialisé avec le chemin de données : {data_path}"
        )

    def ensure_sessions_file(self):
        """
        Vérifie que le fichier des sessions existe et le crée s'il n'existe pas.
        """
        if (
            not os.path.exists(self.sessions_file)
            or os.stat(self.sessions_file).st_size == 0
        ):
            with open(self.sessions_file, "w") as f:
                json.dump([], f)
            print(
                f"Fichier {self.sessions_file} créé pour stocker les sessions de tournoi."
            )

    def load_sessions(self):
        """
        Charge les sessions de tournoi à partir du fichier JSON.

        Returns:
            list: Liste des sessions de tournoi.
        """
        self.ensure_sessions_file()
        with open(self.sessions_file, "r") as f:
            return json.load(f)

    def save_sessions(self, sessions):
        """
        Sauvegarde les sessions de tournoi dans le fichier JSON.

        Args:
            sessions (list): Liste des sessions de tournoi à sauvegarder.
        """
        with open(self.sessions_file, "w") as f:
            json.dump(sessions, f, indent=4)
        print(f"Sessions sauvegardées dans {self.sessions_file}")

    def get_next_id(self):
        """
        Génère le prochain ID pour une nouvelle session de tournoi.

        Returns:
            int: Prochain ID de session de tournoi.
        """
        sessions = self.load_sessions()
        if not sessions:
            return 1
        max_id = max(session["id"] for session in sessions)
        return max_id + 1

    def start_tournament_session(self, tournament_id, player_ids):
        """
        Démarre une nouvelle session de tournoi.

        Args:
            tournament_id (int): ID du tournoi.
            player_ids (list): Liste des IDs des joueurs participant au tournoi.

        Returns:
            dict: Nouvelle session de tournoi.
        """
        sessions = self.load_sessions()
        new_session = {
            "id": self.get_next_id(),
            "tournament_id": tournament_id,
            "player_ids": player_ids,
            "is_active": True,
        }
        sessions.append(new_session)
        self.save_sessions(sessions)
        print(f"Nouvelle session de tournoi démarrée avec l'ID {new_session['id']}")
        return new_session

    def start_tournament_rounds(self, session_id, player_ids, players):
        """
        Démarre les rondes de tournoi pour une session donnée.

        Args:
            session_id (int): ID de la session de tournoi.
            player_ids (list): Liste des IDs des joueurs participant au tournoi.
            players (list): Liste des joueurs participant au tournoi.

        Returns:
            tuple: Scores des joueurs et liste des résultats des rondes.
        """
        player_scores, rounds = self.round_model.start_tournament(
            session_id, player_ids, players
        )
        print(f"Rondes de tournoi démarrées pour la session {session_id}")
        return player_scores, rounds
