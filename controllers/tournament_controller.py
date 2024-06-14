import json
import os


class TournamentController:
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
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_tournament(self, name, location, date):
        data = self.load_data()
        new_id = max([t["id"] for t in data], default=0) + 1
        new_tournament = {
            "id": new_id,
            "name": name,
            "location": location,
            "date": date,
            "is_finished": False,
        }
        data.append(new_tournament)
        self.save_data(data)

    def list_tournaments(self):
        return self.load_data()
