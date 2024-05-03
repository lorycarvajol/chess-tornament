from InquirerPy import prompt
from InquirerPy.utils import color_print
from views.player_views import player_menu

# Si vous avez d'autres menus, par exemple pour les tournois
# from views.tournament_views import tournament_menu


def main_menu():
    while True:
        color_print([("blue", "\n=== Main Menu ===")])
        options = [
            {"name": "Player Management", "value": "player"},
            {"name": "Tournament Management", "value": "tournament"},
            {"name": "Exit", "value": "exit"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "menu",
                "message": "Please choose an option:",
                "choices": options,
            }
        )

        if result["menu"] == "player":
            player_menu()
        # Décommentez le bloc suivant pour gérer les tournois
        # elif result["menu"] == "tournament":
        #     tournament_menu()
        elif result["menu"] == "exit":
            color_print([("green", "Thank you for using the application. Goodbye!")])
            break
        else:
            color_print([("red", "Invalid option, please try again.")])


if __name__ == "__main__":
    main_menu()
