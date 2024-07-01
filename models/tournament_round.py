import itertools
import random
import json
import os
from fpdf import FPDF
from InquirerPy import prompt


class TournamentRoundModel:

    def __init__(self, data_path):
        self.data_path = data_path
        self.file_path = os.path.join(self.data_path, "tournament_round.json")
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_data(self):
        self.ensure_file_exists()
        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_data(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
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

                # Ask the user to select the winner
                winner_name = self.select_match_winner(player1, player2)
                if winner_name == "Generate Report":
                    return (
                        player_scores,
                        rounds,
                        True,
                    )  # Return a flag indicating to generate a report

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

        # Print final results
        self.print_final_results(player_scores, players, rounds)

        # Generate PDF report
        self.generate_pdf_report(
            session_id, player_scores, players, rounds, replace_existing=True
        )
        return player_scores, rounds, False

    def select_match_winner(self, player1, player2):
        question = [
            {
                "type": "list",
                "name": "winner",
                "message": f"Select the winner between {player1} and {player2}:",
                "choices": [player1, player2, "Generate Report"],
            }
        ]
        answer = prompt(question)
        return answer["winner"]

    def get_player_name(self, player_id, players):
        for player in players:
            if player["id"] == player_id:
                return f"{player['first_name']} {player['last_name']}"
        return "Unknown Player"

    def get_rounds(self, session_id):
        rounds = self.load_data()
        return [round for round in rounds if round["session_id"] == session_id]

    def calculate_player_scores(self, session_id):
        rounds = self.get_rounds(session_id)
        player_scores = {}
        for round in rounds:
            for match in round["results"]:
                winner = match["winner"]
                if winner not in player_scores:
                    player_scores[winner] = 0
                player_scores[winner] += 1
        return player_scores

    def get_players(self):
        with open(
            os.path.join(self.data_path, "players.json"), "r", encoding="utf-8"
        ) as f:
            return json.load(f)

    def print_final_results(self, player_scores, players, rounds):
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

    def generate_pdf_report(
        self, session_id, player_scores, players, rounds, replace_existing=False
    ):
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
        if replace_existing:
            pdf_output_path = pdf_output_path.replace(".pdf", "_final.pdf")
        os.makedirs(os.path.dirname(pdf_output_path), exist_ok=True)
        pdf.output(pdf_output_path)
        print(f"\nPDF report generated: {pdf_output_path}")
