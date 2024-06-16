from InquirerPy.utils import color_print
from views.main_menu import main_menu


def print_instructions():

    color_print(
        [("magenta", "Bienvenue dans le gestionnaire de tournois de jeux d'échecs !\n")]
    )

    color_print(
        [("cyan", "Utilisez les options du menu pour naviguer dans l'application.\n")]
    )

    color_print([("yellow", "Instructions:\n")])
    color_print(
        [("green", "1. Pour gérer les joueurs, choisissez 'Player Manager'.\n")]
    )
    color_print(
        [("green", "2. Pour gérer les tournois, choisissez 'Tournament Manager'.\n")]
    )
    color_print(
        [
            (
                "green",
                "3. Suivez les Instructions pour ajouter, lister ou jouer des tournois.\n",
            )
        ]
    )
    color_print(
        [
            (
                "green",
                "4. Pour ajouter un joueur, entrez uniquement des lettres pour le prénom et le nom.\n",
            )
        ]
    )
    color_print([("green", "5. Les dates doivent être au format DD-MM-YYYY.\n")])

    color_print([("blue", "Profitez de l'application!\n")])


if __name__ == "__main__":
    print_instructions()
    main_menu()
