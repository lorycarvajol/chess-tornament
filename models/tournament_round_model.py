import json
import os


class TournamentRoundModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.file_path = os.path.join(self.data_path, "tournament_round.json")
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
