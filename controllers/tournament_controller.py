from tinydb import TinyDB, Query
from models.tournament import Tournament

db = TinyDB("data/db.json")
tournaments_table = db.table("tournaments")

def create_tournament(name, location, start_date, end_date, num_rounds=4, description=""):
    tournament = Tournament(name, location, start_date, end_date, num_rounds, description)
    tournaments_table.insert(tournament.__dict__)
