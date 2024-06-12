from datetime import datetime


class TournamentSession:

    def __init__(
        self,
        tournament_id,
        tournament_name,
        location,
        date,
        players=None,
        is_active=True,
    ):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.location = location
        self.date = datetime.strptime(date, "%d-%m-%Y").date()
        self.is_active = is_active
        self.players = players if players is not None else []

    def add_player(self, player):
        self.players.append(
            {
                "player_id": player.id,
                "first_name": player.first_name,
                "last_name": player.last_name,
                "score": 0,
            }
        )

    def to_dict(self):
        return {
            "tournament_id": self.tournament_id,
            "tournament_name": self.tournament_name,
            "location": self.location,
            "date": self.date.strftime("%d-%m-%Y"),
            "is_active": self.is_active,
            "players": self.players,
        }

    @staticmethod
    def from_dict(data):
        return TournamentSession(
            tournament_id=data["tournament_id"],
            tournament_name=data["tournament_name"],
            location=data["location"],
            date=data["date"],
            players=data.get("players", []),
            is_active=data.get("is_active", True),
        )
