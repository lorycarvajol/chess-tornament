from controllers.player_controller import add_player_form, list_all_players


class AddPlayerCommand:
    def execute(self):
        add_player_form()


class ListPlayersCommand:
    def execute(self):
        list_all_players()
