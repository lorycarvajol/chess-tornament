# commands/tournament_commands.py
from views.tournament_views import (
    add_tournament_form,
    start_tournament_form,
    list_tournaments,
    add_players_to_tournament_form,
)


class AddTournamentCommand:
    def execute(self):
        add_tournament_form()


class PlayTournamentCommand:
    def execute(self):
        start_tournament_form()


class ListTournamentsCommand:
    def execute(self):
        list_tournaments()


class AddPlayersToTournamentCommand:
    def execute(self):
        add_players_to_tournament_form()
