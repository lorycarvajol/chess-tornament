import itertools
import random
import json
import os
from fpdf import FPDF
from InquirerPy import prompt


class TournamentRoundModel:
    def __init__(self, data_path):
        """
        Initialise le modèle des rondes de tournoi avec le chemin vers les données.

        Args:
            data_path (str): Chemin vers le répertoire des données.
        """
        self.data_path = data_path
        self.file_path = os.path.join(self.data_path, "tournament_round.json")
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        S'assure que le fichier JSON des rondes de tournoi existe.
        Si le fichier n'existe pas ou est vide, il est créé.
        """
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def load_data(self):
        """
        Charge les données du fichier JSON des rondes de tournoi.

        Returns:
            list: Liste des données des rondes de tournoi.
        """
        self.ensure_file_exists()
        with open(self.file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_data(self, data):
        """
        Sauvegarde les données dans le fichier JSON des rondes de tournoi.

        Args:
            data (list): Liste des données des rondes de tournoi à sauvegarder.
        """
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def start_tournament(self, session_id, player_ids, players):
        """
        Démarre le tournoi en générant les rondes et en enregistrant les résultats des matchs.

        Args:
            session_id (int): ID de la session de tournoi.
            player_ids (list): Liste des IDs des joueurs participant au tournoi.
            players (list): Liste des joueurs avec leurs informations.

        Returns:
            dict, list: Dictionnaire des scores des joueurs et liste des rondes avec leurs résultats.
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
                player1 = self.get_player_name(match[0], players)
                player2 = self.get_player_name(match[1], players)

                # Demander à l'utilisateur de sélectionner le vainqueur
                winner_name = self.select_match_winner(player1, player2)
                winner_id = match[0] if winner_name == player1 else match[1]
                player_scores[winner_id] += 1

                round_results.append(
                    {"player1": match[0], "player2": match[1], "winner": winner_id}
                )

            tournament_rounds = self.load_data()
            tournament_rounds.append(
                {
                    "session_id": session_id,
                    "round_number": round_number,
                    "results": round_results,
                }
            )
            self.save_data(tournament_rounds)

            rounds.append({"round_number": round_number, "results": round_results})

            round_number += 1

        # Afficher les résultats finaux
        self.print_final_results(player_scores, players, rounds)

        # Générer un rapport PDF
        self.generate_pdf_report(session_id, player_scores, players, rounds)
        return player_scores, rounds

    def select_match_winner(self, player1, player2):
        """
        Demande à l'utilisateur de sélectionner le vainqueur d'un match.

        Args:
            player1 (str): Nom du premier joueur.
            player2 (str): Nom du deuxième joueur.

        Returns:
            str: Nom du joueur vainqueur.
        """
        question = [
            {
                "type": "list",
                "name": "winner",
                "message": f"Select the winner between {player1} and {player2}:",
                "choices": [player1, player2],
            }
        ]
        answer = prompt(question)
        return answer["winner"]

    def get_player_name(self, player_id, players):
        """
        Obtient le nom complet d'un joueur à partir de son ID.

        Args:
            player_id (int): ID du joueur.
            players (list): Liste des joueurs avec leurs informations.

        Returns:
            str: Nom complet du joueur.
        """
        for player in players:
            if player["id"] == player_id:
                return f"{player['first_name']} {player['last_name']}"
        return "Unknown Player"

    def print_final_results(self, player_scores, players, rounds):
        """
        Affiche les résultats finaux du tournoi dans la console.

        Args:
            player_scores (dict): Dictionnaire des scores des joueurs.
            players (list): Liste des joueurs avec leurs informations.
            rounds (list): Liste des rondes avec leurs résultats.
        """
        print("\nTournament Results:")
        print("Final Scores:")
        for player_id, score in player_scores.items():
            player_name = self.get_player_name(player_id, players)
            print(f"{player_name}: {score} points")

        winner_id = max(player_scores, key=player_scores.get)
        winner_name = self.get_player_name(winner_id, players)
        print(f"\nWinner: {winner_name} with {player_scores[winner_id]} points")

        print("\nMatch Results by Round:")
        for round_info in rounds:
            print(f"\nRound {round_info['round_number']}:")
            for match in round_info["results"]:
                player1 = self.get_player_name(match["player1"], players)
                player2 = self.get_player_name(match["player2"], players)
                winner = self.get_player_name(match["winner"], players)
                print(f"{player1} vs {player2} - Winner: {winner}")

    def generate_pdf_report(self, session_id, player_scores, players, rounds):
        """
        Génère un rapport PDF des résultats du tournoi.

        Args:
            session_id (int): ID de la session de tournoi.
            player_scores (dict): Dictionnaire des scores des joueurs.
            players (list): Liste des joueurs avec leurs informations.
            rounds (list): Liste des rondes avec leurs résultats.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Tournament Results", ln=True, align="C")

        pdf.cell(200, 10, txt="Final Scores:", ln=True, align="L")
        for player_id, score in player_scores.items():
            player_name = self.get_player_name(player_id, players)
            pdf.cell(200, 10, txt=f"{player_name}: {score} points", ln=True, align="L")

        winner_id = max(player_scores, key=player_scores.get)
        winner_name = self.get_player_name(winner_id, players)
        pdf.cell(
            200,
            10,
            txt=f"\nWinner: {winner_name} with {player_scores[winner_id]} points",
            ln=True,
            align="L",
        )

        pdf.cell(200, 10, txt="\nMatch Results by Round:", ln=True, align="L")
        for round_info in rounds:
            pdf.cell(
                200,
                10,
                txt=f"\nRound {round_info['round_number']}:",
                ln=True,
                align="L",
            )
            for match in round_info["results"]:
                player1 = self.get_player_name(match["player1"], players)
                player2 = self.get_player_name(match["player2"], players)
                winner = self.get_player_name(match["winner"], players)
                pdf.cell(
                    200,
                    10,
                    txt=f"{player1} vs {player2} - Winner: {winner}",
                    ln=True,
                    align="L",
                )

        pdf_output_path = os.path.join(
            self.data_path, "rapport", f"tournament_session_{session_id}_report.pdf"
        )
        os.makedirs(os.path.dirname(pdf_output_path), exist_ok=True)
        pdf.output(pdf_output_path)
        print(f"\nPDF report generated: {pdf_output_path}")
