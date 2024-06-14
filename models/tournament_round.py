import json
import os
import itertools
import random
from datetime import datetime
from InquirerPy import prompt
from fpdf import FPDF


class TournamentRoundModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.file_path = os.path.join(self.data_path, "tournament_rounds.json")
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def load_data(self):
        self.ensure_file_exists()
        with open(self.file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def start_tournament(self, session_id, player_ids, players):
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

        self.display_results(player_scores, players, rounds)
        self.generate_pdf_report(session_id, player_scores, players, rounds)
        return player_scores, rounds

    def get_player_name(self, player_id, players):
        for player in players:
            if player["id"] == player_id:
                return f"{player['first_name']} {player['last_name']}"
        return "Unknown Player"

    def select_match_winner(self, player1, player2):
        winner = prompt(
            [
                {
                    "type": "list",
                    "name": "winner",
                    "message": f"Select the winner between {player1} and {player2}:",
                    "choices": [player1, player2],
                }
            ]
        )["winner"]
        return winner

    def display_results(self, player_scores, players, rounds):
        print("\nTournament Results:")
        print("Final Scores:")
        for player_id, score in player_scores.items():
            player_name = self.get_player_name(player_id, players)
            print(f"{player_name}: {score} points")
        winner_id = max(player_scores, key=player_scores.get)
        winner_name = self.get_player_name(winner_id, players)
        print(f"\nWinner: {winner_name} with {player_scores[winner_id]} points")

        print("\nMatch Results by Round:")
        for rnd in rounds:
            print(f"\nRound {rnd['round_number']}:")
            for result in rnd["results"]:
                player1 = self.get_player_name(result["player1"], players)
                player2 = self.get_player_name(result["player2"], players)
                winner = self.get_player_name(result["winner"], players)
                print(f"{player1} vs {player2} - Winner: {winner}")

    def generate_pdf_report(self, session_id, player_scores, players, rounds):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(
            200,
            10,
            txt=f"Tournament Session Report - ID: {session_id}",
            ln=True,
            align="C",
        )
        pdf.ln(10)

        pdf.cell(200, 10, txt="Final Scores:", ln=True)
        for player_id, score in player_scores.items():
            player_name = self.get_player_name(player_id, players)
            pdf.cell(200, 10, txt=f"{player_name}: {score} points", ln=True)

        winner_id = max(player_scores, key=player_scores.get)
        winner_name = self.get_player_name(winner_id, players)
        pdf.ln(10)
        pdf.cell(
            200,
            10,
            txt=f"Winner: {winner_name} with {player_scores[winner_id]} points",
            ln=True,
        )

        pdf.ln(10)
        pdf.cell(200, 10, txt="Match Results by Round:", ln=True)
        for rnd in rounds:
            pdf.ln(5)
            pdf.cell(200, 10, txt=f"Round {rnd['round_number']}:", ln=True)
            for result in rnd["results"]:
                player1 = self.get_player_name(result["player1"], players)
                player2 = self.get_player_name(result["player2"], players)
                winner = self.get_player_name(result["winner"], players)
                pdf.cell(
                    200, 10, txt=f"{player1} vs {player2} - Winner: {winner}", ln=True
                )

        pdf_output_path = os.path.join(
            self.data_path, f"tournament_session_{session_id}_report.pdf"
        )
        pdf.output(pdf_output_path)
        print(f"\nPDF report generated: {pdf_output_path}")
