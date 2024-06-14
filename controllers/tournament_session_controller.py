import os
import json
from models.tournament_round import TournamentRoundModel


class TournamentSessionController:
    def __init__(self, data_path):
        self.data_path = data_path
        self.sessions_file = os.path.join(self.data_path, "tournament_sessions.json")
        self.round_model = TournamentRoundModel(self.data_path)
        self.ensure_sessions_file()

    def ensure_sessions_file(self):
        if (
            not os.path.exists(self.sessions_file)
            or os.stat(self.sessions_file).st_size == 0
        ):
            with open(self.sessions_file, "w") as f:
                json.dump([], f)

    def load_sessions(self):
        self.ensure_sessions_file()
        with open(self.sessions_file, "r") as f:
            return json.load(f)

    def save_sessions(self, sessions):
        with open(self.sessions_file, "w") as f:
            json.dump(sessions, f, indent=4)

    def get_next_id(self):
        sessions = self.load_sessions()
        if not sessions:
            return 1
        max_id = max(session["id"] for session in sessions)
        return max_id + 1

    def start_tournament_session(self, tournament_id, player_ids):
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

    def start_tournament_rounds(self, session_id, player_ids, players):
        player_scores, rounds = self.round_model.start_tournament(
            session_id, player_ids, players
        )
        return player_scores, rounds
