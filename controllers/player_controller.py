import json
import os
from models.player import Player


class PlayerController:
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

    def add_player(self, first_name, last_name, birthdate):
        data = self.load_data()
        new_id = max([p["id"] for p in data], default=0) + 1
        new_player = Player(first_name, last_name, birthdate, new_id).to_dict()
        data.append(new_player)
        self.save_data(data)

    def list_players(self):
        return self.load_data()
