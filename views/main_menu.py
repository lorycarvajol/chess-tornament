from InquirerPy import prompt
from views.tournament_views import tournament_manager_menu
from views.player_views import player_manager_menu


def main_menu():
    while True:
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
            break
