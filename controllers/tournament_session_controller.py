import os
import json
from models.tournament_round import TournamentRoundModel


class TournamentSessionController:
    def __init__(self, data_path):
        """
        Initialise le contrôleur de session de tournoi avec le chemin du fichier de données.

        Args:
            data_path (str): Chemin vers le répertoire où les données sont stockées.
        """
        self.data_path = data_path
        self.sessions_file = os.path.join(self.data_path, "tournament_sessions.json")
        self.round_model = TournamentRoundModel(self.data_path)
        self.ensure_sessions_file()

    def ensure_sessions_file(self):
        """
        Vérifie si le fichier des sessions existe et s'il est vide, il crée un fichier vide.
        """
        if (
            not os.path.exists(self.sessions_file)
            or os.stat(self.sessions_file).st_size == 0
        ):
            with open(self.sessions_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_sessions(self):
        """
        Charge les sessions de tournoi depuis le fichier JSON.

        Returns:
            list: Une liste des sessions de tournoi.
        """
        self.ensure_sessions_file()
        with open(self.sessions_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_sessions(self, sessions):
        """
        Sauvegarde les sessions de tournoi dans le fichier JSON.

        Args:
            sessions (list): Les sessions de tournoi à sauvegarder.
        """
        with open(self.sessions_file, "w", encoding="utf-8") as f:
            json.dump(sessions, f, indent=4)

    def get_next_id(self):
        """
        Génère le prochain ID disponible pour une nouvelle session de tournoi.

        Returns:
            int: Le prochain ID disponible.
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
            tournament_id (int): L'ID du tournoi.
            player_ids (list): Une liste des IDs des joueurs participant au tournoi.

        Returns:
            dict: La nouvelle session de tournoi.
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
        return new_session

    def generate_pdf_report(self, session_id, replace_existing=False):
        """
        Génère un rapport PDF pour une session de tournoi spécifique.

        Args:
            session_id (int): L'ID de la session de tournoi.
            replace_existing (bool): Indique s'il faut remplacer le rapport existant (pour le rapport final).
        """
        sessions = self.load_sessions()
        session = next((s for s in sessions if s["id"] == session_id), None)
        if not session:
            print(f"Aucune session trouvée avec l'ID {session_id}.")
            return

        players = self.round_model.get_players()
        player_ids = session["player_ids"]
        player_scores = self.round_model.calculate_player_scores(session_id)
        rounds = self.round_model.get_rounds(session_id)

        self.round_model.generate_pdf_report(
            session_id, player_scores, players, rounds, replace_existing
        )
        print(f"Rapport PDF généré pour la session ID {session_id}.")
