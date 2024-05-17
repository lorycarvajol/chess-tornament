# commands/tournament_commands.py
from controllers.tournament_controller import (
    add_tournament,
    load_active_tournaments,
    play_tournament,
)
from views.tournament_views import add_tournament_form, start_tournament_form
from InquirerPy.utils import color_print


class AddTournamentCommand:
    def execute(self):
        add_tournament_form()


class PlayTournamentCommand:
    def execute(self):
        start_tournament_form()


class ListTournamentsCommand:
    def execute(self):
        tournaments = load_active_tournaments()
        if tournaments:
            color_print([("cyan", "Active Tournaments:")])
            for tournament in tournaments:
                color_print(
                    [
                        (
                            "yellow",
                            f"{tournament.name} - {tournament.location} on {tournament.date}",
                        )
                    ]
                )
        else:
            color_print([("red", "No active tournaments available.")])
