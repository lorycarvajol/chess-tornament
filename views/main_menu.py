from InquirerPy import prompt
from InquirerPy.utils import color_print
from commands.player_commands import AddPlayerCommand, ListPlayersCommand
from commands.tournament_commands import AddTournamentCommand

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
            AddPlayerCommand().execute()
        elif result == "list_players":
            ListPlayersCommand().execute()
        elif result == "return":
            break


def tournament_manager_menu():
    while True:
        color_print([("blue", "\nTournament Manager Menu")])
        options = [
            {"name": "Add Tournament", "value": "add_tournament"},
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
            AddTournamentCommand().execute()

        elif result == "return":
            break


if __name__ == "__main__":
    main_menu()
