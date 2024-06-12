from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.player_controller import add_player_form, list_all_players


def player_manager_menu():
    while True:
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
            add_player_form()
        elif result == "list_players":
            list_all_players()
        elif result == "return":
            break
