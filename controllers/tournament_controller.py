from models.tournament import Tournament
from tinydb import TinyDB, Query


class TournamentController:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.tournaments = self.db.table("tournaments")

    def add_tournament(self, name, location, date):
        new_tournament = Tournament(name, location, date)
        self.tournaments.insert(new_tournament.to_dict())
        return new_tournament

    def list_tournaments(self):
        return self.tournaments.all()
