from InquirerPy import prompt
from InquirerPy.utils import color_print
from views.player_views import player_menu
from views.tournament_views import tournament_menu


def main_menu():
    """
    Affiche le menu principal et gère la navigation entre les différentes sections de l'application.
    """
    while True:
        # Affiche un message d'instructions à l'utilisateur
        color_print([("blue", "Main Menu - Choose an option to proceed.")])

        # Définit les options du menu principal
        options = [
            {"name": "Player Manager", "value": "player_manager"},
            {"name": "Tournament Manager", "value": "tournament_manager"},
            {"name": "Exit", "value": "exit"},
        ]

        # Affiche le menu et attend la sélection de l'utilisateur
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Select an option:",
                "choices": options,
            }
        )["action"]

        # En fonction de la sélection de l'utilisateur, appelle la fonction correspondante
        if result == "player_manager":
            player_menu()  # Appelle le menu de gestion des joueurs
        elif result == "tournament_manager":
            tournament_menu()  # Appelle le menu de gestion des tournois
        elif result == "exit":
            break  # Quitte l'application
