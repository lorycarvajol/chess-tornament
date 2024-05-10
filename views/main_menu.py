from InquirerPy import prompt
from InquirerPy.utils import color_print
from views.player_views import add_player_form, list_players
from views.tournament_views import (
    add_tournament_form,
    list_tournaments,
    play_tournament,
)


def main_menu():
    while True:
        color_print([("blue", "\nMain Menu")])
        options = [
            {"name": "Player Manager", "value": "player_manager"},
            {"name": "Tournament Manager", "value": "tournament_manager"},
            {"name": "Exit", "value": "exit"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Select an option:",
                "choices": options,
            }
        )["action"]

        if result == "player_manager":
            player_manager_menu()
        elif result == "tournament_manager":
            tournament_manager_menu()
        elif result == "exit":
            color_print([("red", "Exiting the application...")])
            break


def player_manager_menu():
    while True:
        color_print([("blue", "\nPlayer Manager Menu")])
        options = [
            {"name": "Add Player", "value": "add_player"},
            {"name": "List Players", "value": "list_players"},
            {"name": "Return to Main Menu", "value": "return"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Select an option:",
                "choices": options,
            }
        )["action"]

        if result == "add_player":
            try:
                add_player_form()
            except Exception as e:
                color_print([("red", f"Error adding player: {str(e)}")])
        elif result == "list_players":
            list_players()
        elif result == "return":
            break


def tournament_manager_menu():
    while True:
        color_print([("blue", "\nTournament Manager Menu")])
        options = [
            {"name": "Add Tournament", "value": "add_tournament"},
            {"name": "List Tournaments", "value": "list_tournaments"},
            {"name": "Play Tournament", "value": "play_tournament"},
            {"name": "Return to Main Menu", "value": "return"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Select an option:",
                "choices": options,
            }
        )["action"]

        if result == "add_tournament":
            try:
                add_tournament_form()
            except Exception as e:
                color_print([("red", f"Error adding tournament: {str(e)}")])
        elif result == "list_tournaments":
            list_tournaments()
        elif result == "play_tournament":
            play_tournament()
        elif result == "return":
            break


if __name__ == "__main__":
    main_menu()
