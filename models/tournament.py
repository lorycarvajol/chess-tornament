from datetime import datetime
from models.match import Match
from models.round import Round
from models.player import Player


class Tournament:
    """Classe représentant un tournoi avec des joueurs et des rondes."""

    def __init__(self, name, location, date, players=None, rounds=None):
        self.name = name
        self.location = location
        try:
            # Assurer que la date est correctement formatée
            self.date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")

        # Initialiser la liste des joueurs et des rondes
        self.players = players if players is not None else []
        self.rounds = rounds if rounds is not None else []

    def add_player(self, player):
        """Ajouter un joueur au tournoi en évitant les doublons."""
        if player not in self.players:
            self.players.append(player)

    def create_round(self):
        """Créer une nouvelle ronde en appariant les joueurs."""
        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)
        matches = []

        # Gérer les "byes" si le nombre de joueurs est impair
        if len(sorted_players) % 2 != 0:
            sorted_players.append(None)

        # Créer les paires de joueurs
        for i in range(0, len(sorted_players), 2):
            if sorted_players[i + 1] is None:
                print(f"{sorted_players[i].first_name} has a bye.")
            else:
                matches.append(Match(sorted_players[i], sorted_players[i + 1]))

        # Créer une nouvelle ronde et l'ajouter à la liste des rondes
        new_round = Round(len(self.rounds) + 1, matches)
        self.rounds.append(new_round)
        return new_round

    def to_dict(self):
        """Convertir l'objet Tournament en dictionnaire pour la sérialisation."""
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
            "players": [player.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }

    @staticmethod
    def from_dict(data):
        """Créer un objet Tournament à partir d'un dictionnaire."""
        return Tournament(
            name=data["name"],
            location=data["location"],
            date=data["date"],
            players=[Player.from_dict(p) for p in data["players"]],
            rounds=[Round.from_dict(r) for r in data["rounds"]],
        )
