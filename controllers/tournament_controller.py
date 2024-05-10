from models.tournament import Tournament
from models.round import Round
from models.player import Player
from tinydb import TinyDB, Query


class TournamentController:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.tournaments = self.db.table("tournaments")

    def find_tournament_by_name(self, name):
        TournamentQuery = Query()
        result = self.tournaments.search(TournamentQuery.name == name)
        if result:
            data = result[0]
            return Tournament(
                name=data["name"],
                location=data["location"],
                date=data["date"],
                players=data.get("players", []),
                rounds=data.get("rounds", []),
            )
        return None
