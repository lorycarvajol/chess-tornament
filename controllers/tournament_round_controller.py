import itertools
import os
import random
from models.tournament_round_model import TournamentRoundModel
from controllers.tournament_session_controller import TournamentSessionController
from controllers.player_controller import PlayerController


class TournamentRoundController:
    def __init__(self, data_path):
        self.round_model = TournamentRoundModel(data_path)
        self.session_controller = TournamentSessionController(data_path)
        self.player_controller = PlayerController(
            os.path.join(data_path, "players.json")
        )

    def get_player_name(self, player_id, players):
        player = next((p for p in players if p["id"] == player_id), None)
        if player:
            return f"{player['first_name']} {player['last_name']}"
        return "Unknown Player"

    def start_tournament(self, session_id, player_ids):
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

        return player_scores, rounds

    def select_match_winner(self, player1, player2):
        print(f"Match: {player1} vs {player2}")
        winner = input(f"Enter the winner ({player1}/{player2}): ")
        while winner not in [player1, player2]:
            winner = input(f"Invalid input. Enter the winner ({player1}/{player2}): ")
        return winner
