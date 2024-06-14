from InquirerPy import prompt
from InquirerPy.utils import color_print
from views.player_views import player_menu
from views.tournament_views import tournament_menu


def main_menu():
    while True:
        color_print([("blue", "Main Menu - Choose an option to proceed.")])
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
            player_menu()
        elif result == "tournament_manager":
            tournament_menu()
        elif result == "exit":
            break
