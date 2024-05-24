from controllers.player_controller import (
    add_player_form,
    list_all_players,
    load_all_players,
)


class AddPlayerCommand:
    def execute(self):
        add_player_form()


class ListPlayersCommand:
    def execute(self):
        list_all_players()


def list_all_players():
    players = load_all_players()
    for player in players:
        print(f"{player.first_name} {player.last_name}, born on {player.birthdate}")
