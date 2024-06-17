import itertools
import os
import random
from models.tournament_round import TournamentRoundModel
from controllers.tournament_session_controller import TournamentSessionController
from controllers.player_controller import PlayerController


class TournamentRoundController:
    def __init__(self, data_path):
        """
        Initialise le contrôleur des rondes de tournoi avec le chemin des données.

        Args:
            data_path (str): Chemin vers le dossier contenant les données des tournois.
        """
        self.round_model = TournamentRoundModel(data_path)
        self.session_controller = TournamentSessionController(data_path)
        self.player_controller = PlayerController(
            os.path.join(data_path, "players.json")
        )

    def get_player_name(self, player_id, players):
        """
        Récupère le nom complet d'un joueur à partir de son ID.

        Args:
            player_id (int): ID du joueur.
            players (list): Liste des joueurs.

        Returns:
            str: Nom complet du joueur ou 'Unknown Player' si le joueur n'est pas trouvé.
        """
        player = next((p for p in players if p["id"] == player_id), None)
        if player:
            return f"{player['first_name']} {player['last_name']}"
        return "Unknown Player"

    def start_tournament(self, session_id, player_ids):
        """
        Démarre le tournoi en générant et en jouant les rondes.

        Args:
            session_id (int): ID de la session de tournoi.
            player_ids (list): Liste des IDs des joueurs participant au tournoi.

        Returns:
            dict: Scores des joueurs.
            list: Liste des résultats des rondes.
        """
        player_scores = {player_id: 0 for player_id in player_ids}
        round_number = 1
        all_matches = list(itertools.combinations(player_ids, 2))
        random.shuffle(all_matches)
        rounds = []

        while all_matches:
            matches = all_matches[: len(player_ids) // 2]
            all_matches = all_matches[len(player_ids) // 2 :]
            round_results = []

            for match in matches:
                player1 = self.get_player_name(
                    match[0], self.player_controller.list_players()
                )
                player2 = self.get_player_name(
                    match[1], self.player_controller.list_players()
                )
                winner_name = self.select_match_winner(player1, player2)
                winner_id = match[0] if winner_name == player1 else match[1]
                player_scores[winner_id] += 1
                round_results.append(
                    {"player1": match[0], "player2": match[1], "winner": winner_id}
                )

            tournament_rounds = self.round_model.load_data()
            tournament_rounds.append(
                {
                    "session_id": session_id,
                    "round_number": round_number,
                    "results": round_results,
                }
            )
            self.round_model.save_data(tournament_rounds)

            rounds.append({"round_number": round_number, "results": round_results})
            round_number += 1

        print(f"Tournoi terminé. Session ID: {session_id}")
        return player_scores, rounds

    def select_match_winner(self, player1, player2):
        """
        Sélectionne le gagnant d'un match en demandant à l'utilisateur.

        Args:
            player1 (str): Nom du premier joueur.
            player2 (str): Nom du deuxième joueur.

        Returns:
            str: Nom du joueur gagnant.
        """
        print(f"Match: {player1} vs {player2}")
        winner = input(f"Entrez le gagnant ({player1}/{player2}): ")
        while winner not in [player1, player2]:
            print("Entrée invalide. Veuillez réessayer.")
            winner = input(f"Entrez le gagnant ({player1}/{player2}): ")
        return winner
