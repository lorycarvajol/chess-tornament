from datetime import datetime


class Tournament:
    _id_counter = 0  # Attribut de classe pour suivre l'ID actuel

    def __init__(self, name, location, date, players=None, is_finished=False):
        """
        Initialise un tournoi.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            date (str): Date du tournoi au format "DD-MM-YYYY".
            players (list, optional): Liste des ID des joueurs participant au tournoi. Par défaut, None.
            is_finished (bool, optional): Indique si le tournoi est terminé. Par défaut, False.
        """
        self.id = Tournament._get_next_id()
        self.name = name
        self.location = location
        try:
            self.date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")
        self.players = players if players is not None else []
        self.is_finished = is_finished

    @classmethod
    def _get_next_id(cls):
        """
        Génère le prochain ID pour le tournoi.

        Returns:
            int: Prochain ID.
        """
        cls._id_counter += 1
        return cls._id_counter

    def add_player(self, player_id):
        """
        Ajoute un joueur au tournoi.

        Args:
            player_id (int): ID du joueur à ajouter.
        """
        if player_id not in self.players:
            self.players.append(player_id)

    def to_dict(self):
        """
        Convertit le tournoi en dictionnaire.

        Returns:
            dict: Dictionnaire représentant le tournoi.
        """
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
            "players": self.players,
            "is_finished": self.is_finished,
        }

    @staticmethod
    def from_dict(data):
        """
        Crée une instance de Tournament à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du tournoi.

        Returns:
            Tournament: Instance de Tournament.
        """
        tournament = Tournament(
            name=data["name"],
            location=data["location"],
            date=data["date"],
            players=data.get("players", []),
            is_finished=data.get("is_finished", False),
        )
        tournament.id = data.get("id", Tournament._get_next_id())
        Tournament._id_counter = max(Tournament._id_counter, tournament.id)
        return tournament
