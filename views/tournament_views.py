from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import TournamentController
from controllers.tournament_session_controller import TournamentSessionController
from controllers.player_controller import PlayerController
import re
from datetime import datetime

# Initialisation des contrôleurs pour les tournois, les joueurs et les sessions de tournoi
tournament_controller = TournamentController("data/tournaments.json")
player_controller = PlayerController("data/players.json")
session_controller = TournamentSessionController("data")


def validate_date(input_date):
    """
    Valide que la date est au format DD-MM-YYYY et est une date valide.
    """
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", input_date):
        return "La date doit être au format DD-MM-YYYY."
    day, month, year = input_date.split("-")
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return "La date doit contenir des nombres valides."
    if not 1 <= month <= 12:
        return "Le mois doit être entre 01 et 12."
    if not 1 <= day <= 31:
        return "Le jour doit être entre 01 et 31."
    try:
        datetime.strptime(input_date, "%d-%m-%Y")
    except ValueError:
        return "Date invalide. Veuillez vous assurer que le jour, le mois et l'année sont corrects."
    return True


def validate_name(name):
    """
    Valide que le nom contient uniquement des lettres (majuscules et minuscules) et des lettres accentuées.
    """
    if re.match(r"^[A-Za-zÀ-ÿ]+$", name):  # Support des lettres accentuées
        return True
    return "Le nom ne doit contenir que des lettres en majuscule ou en minuscule."


def get_valid_input(message, validate_fn):
    """
    Demande une entrée utilisateur, la valide et affiche un message d'erreur jusqu'à ce que l'entrée soit correcte.
    """
    while True:
        result = prompt({"type": "input", "name": "input", "message": message})["input"]
        validation_message = validate_fn(result)
        if validation_message is True:
            return result.strip().capitalize()
        else:
            color_print([("red", validation_message)])


def add_tournament_form():
    """
    Ajoute un nouveau tournoi à la base de données après avoir validé les entrées.
    """
    color_print([("cyan", "Ajouter un nouveau tournoi à la base de données.")])
    print("Veuillez entrer les détails du tournoi.")
    name = get_valid_input(
        "Entrez le nom du tournoi (lettres seulement) :", validate_name
    )
    location = get_valid_input(
        "Entrez l'emplacement du tournoi (lettres seulement) :", validate_name
    )
    date = get_valid_input("Entrez la date du tournoi (DD-MM-YYYY) :", validate_date)

    tournament_controller.add_tournament(name, location, date)
    color_print([("green", "Tournoi ajouté avec succès !")])


def add_players_to_tournament():
    """
    Ajoute des joueurs à un tournoi existant et démarre une session de tournoi.
    """
    color_print([("cyan", "\nAjouter des joueurs à un tournoi existant.")])

    # Charge la liste des tournois
    tournaments = tournament_controller.list_tournaments()
    if not tournaments:
        color_print([("red", "Aucun tournoi disponible.")])
        return

    # Permet de choisir un tournoi
    tournament_choices = [
        {"name": f"{t['id']}: {t['name']}", "value": t["id"]} for t in tournaments
    ]
    selected_tournament_id = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choisissez un tournoi pour ajouter des joueurs :",
            "choices": tournament_choices,
        }
    )["tournament"]

    # Charge la liste des joueurs
    players = player_controller.list_players()
    if not players:
        color_print([("yellow", "Aucun joueur disponible.")])
        return

    # Permet de choisir des joueurs
    player_choices = [
        {"name": f"{p['first_name']} {p['last_name']}", "value": p["id"]}
        for p in players
    ]
    selected_player_ids = prompt(
        {
            "type": "checkbox",
            "name": "players",
            "message": "Sélectionnez des joueurs pour ce tournoi ( utilisez 'espace' pour sélectionner, 'entrer' pour valider) :",
            "choices": player_choices,
        }
    )["players"]

    if not selected_player_ids:
        color_print([("yellow", "Aucun joueur sélectionné pour le tournoi.")])
        return

    # Démarre une session de tournoi
    session_controller = TournamentSessionController("data")
    session = session_controller.start_tournament_session(
        selected_tournament_id, selected_player_ids
    )

    color_print([("green", f"Session de tournoi commencée avec l'ID {session['id']}")])
    print(
        "Début des rondes du tournoi. Vous allez maintenant sélectionner les vainqueurs des matchs."
    )

    # Démarre les rounds du tournoi
    session_controller.start_tournament_rounds(
        session["id"], selected_player_ids, players
    )


def tournament_menu():
    """
    Menu pour gérer les tournois.
    """
    while True:
        color_print(
            [
                (
                    "blue",
                    "\nMenu du tournoi - Gérer les tournois dans la base de données.",
                )
            ]
        )
        options = [
            {"name": "Ajouter un tournoi", "value": "add"},
            {"name": "Jouer un tournoi", "value": "play"},
            {"name": "Retourner au menu principal", "value": "return"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Sélectionnez une option:",
                "choices": options,
            }
        )["action"]

        if result == "add":
            add_tournament_form()
        elif result == "play":
            add_players_to_tournament()
        elif result == "return":
            break


if __name__ == "__main__":
    print("Bienvenue dans le gestionnaire de tournois !")
    print("Utilisez les options du menu pour naviguer dans l'application.")
    tournament_menu()
