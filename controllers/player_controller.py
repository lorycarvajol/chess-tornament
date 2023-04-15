from tinydb import TinyDB, Query
from models.player import Player

db = TinyDB("data/db.json")
players_table = db.table("players")

def create_player(first_name, last_name, date_of_birth):
    player = Player(first_name, last_name, date_of_birth)
    players_table.insert(player.__dict__)
