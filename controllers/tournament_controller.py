from models.tournament import Tournament
from tinydb import TinyDB, Query


class TournamentController:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.tournaments = self.db.table("tournaments")

    def add_tournament(self, name, location, date):
        """Ajoute un nouveau tournoi à la base de données après validation"""
        new_tournament = Tournament(name, location, date)
        self.tournaments.insert(new_tournament.to_dict())
        return new_tournament

    def list_tournaments(self):
        """Récupère tous les tournois stockés dans la base de données"""
        return self.tournaments.all()

    def find_tournament_by_name(self, name):
        """Trouve un tournoi par son nom"""
        TournamentQuery = Query()
        result = self.tournaments.search(TournamentQuery.name == name)
        return result
