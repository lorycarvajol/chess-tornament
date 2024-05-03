from models.player import Player
from tinydb import TinyDB, Query


class PlayerController:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.players = self.db.table("players")

    def add_player(self, first_name, last_name, date_of_birth, national_id):
        new_player = Player(first_name, last_name, date_of_birth, national_id)
        self.players.insert(new_player.to_dict())
        return new_player

    def list_players(self):
        return self.players.all()
