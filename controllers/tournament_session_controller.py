import json
import os


class TournamentSessionController:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def load_data(self):
        with open(self.file_path, "r") as f:
            try:
                sessions = json.load(f)
                # Ensure each session has an 'id' field
                for session in sessions:
                    if "id" not in session:
                        session["id"] = self.get_next_id(sessions)
                return sessions
            except json.JSONDecodeError:
                return []

    def save_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_next_id(self, sessions):
        if not sessions:
            return 1
        max_id = max(session.get("id", 0) for session in sessions)
        return max_id + 1

    def start_tournament_session(self, tournament_id, player_ids):
        sessions = self.load_data()
        new_session = {
            "id": self.get_next_id(sessions),
            "tournament_id": tournament_id,
            "player_ids": player_ids,
            "is_active": True,
        }
        sessions.append(new_session)
        self.save_data(sessions)
        return new_session
