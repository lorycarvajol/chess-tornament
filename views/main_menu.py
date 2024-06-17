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
        color_print(
            [("blue", "Menu Principal - Choisissez une option pour continuer.")]
        )

        # Définit les options du menu principal
        options = [
            {"name": "Gestion des Joueurs", "value": "player_manager"},
            {"name": "Gestion des Tournois", "value": "tournament_manager"},
            {"name": "Quitter", "value": "exit"},
        ]

        # Affiche le menu et attend la sélection de l'utilisateur
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Sélectionnez une option :",
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

    # Affiche un message sympathique lorsque l'utilisateur quitte l'application
    color_print(
        [
            (
                "green",
                "Merci d'avoir utilisé le gestionnaire de tournois ! À bientôt et bonne chance pour vos prochains tournois !",
            )
        ]
    )


if __name__ == "__main__":
    main_menu()
