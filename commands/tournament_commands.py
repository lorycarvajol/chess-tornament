from controllers.tournament_controller import play_tournament


class PlayTournamentCommand:
    def execute(self):
        play_tournament()


class AddTournamentCommand:
    def execute(self):
        from controllers.tournament_controller import add_tournament_form

        add_tournament_form()
