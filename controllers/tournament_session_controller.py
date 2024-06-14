import os
import json
from models.tournament_round import TournamentRoundModel


class TournamentSessionController:

    def __init__(self, data_path):
        self.data_path = data_path
        self.sessions_file = os.path.join(self.data_path, "tournament_sessions.json")
        self.round_model = TournamentRoundModel(data_path)
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if (
            not os.path.exists(self.sessions_file)
            or os.stat(self.sessions_file).st_size == 0
        ):
            with open(self.sessions_file, "w") as f:
                json.dump([], f)

    def load_sessions(self):
        self.ensure_file_exists()
        with open(self.sessions_file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_sessions(self, sessions):
        with open(self.sessions_file, "w") as f:
            json.dump(sessions, f, indent=4)

    def get_next_id(self):
        sessions = self.load_sessions()
        if not sessions:
            return 1
        max_id = max(session["id"] for session in sessions)
        return max_id + 1

    def start_tournament_session(self, tournament, players):
        sessions = self.load_sessions()
        session_id = self.get_next_id()
        session = {
            "id": session_id,
            "tournament_id": tournament["id"],
            "tournament_name": tournament["name"],
            "location": tournament["location"],
            "date": tournament["date"],
            "is_active": True,
            "players": [
                {
                    "player_id": p["id"],
                    "first_name": p["first_name"],
                    "last_name": p["last_name"],
                    "score": 0,
                }
                for p in players
            ],
        }
        sessions.append(session)
        self.save_sessions(sessions)
        print(f"Tournament session started with ID {session_id}")
        self.round_model.start_tournament(
            session_id, [p["id"] for p in players], players
        )
        return session

    def start_tournament_rounds(self, session_id, player_ids, players):
        return self.round_model.start_tournament(session_id, player_ids, players)
