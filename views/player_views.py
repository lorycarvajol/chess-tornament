from datetime import datetime
from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.player_controller import PlayerController
import re

# Initialisation du contrôleur des joueurs
player_controller = PlayerController("data/players.json")


# Fonction de validation pour la date
def validate_date(input_date):
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", input_date):
        return "Date must be in DD-MM-YYYY format."
    day, month, year = input_date.split("-")
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return "Date must contain valid numbers."
    if not 1 <= month <= 12:
        return "Month must be between 01 and 12."
    if not 1 <= day <= 31:
        return "Day must be between 01 and 31."
    try:
        datetime.strptime(input_date, "%d-%m-%Y")
    except ValueError:
        return "Invalid date. Please ensure the day, month, and year are correct."
    return True


# Fonction de validation pour le nom
def validate_name(name):
    """Valider que le nom ne contient que des lettres."""
    if re.match(r"^[A-Za-zÀ-ÿ]+$", name):  # Support des lettres accentuées
        return True
    return "Name must contain only letters in upper or lower case."


# Fonction pour obtenir une entrée valide de l'utilisateur
def get_valid_input(message, validate_fn):
    while True:
        result = prompt({"type": "input", "name": "input", "message": message})["input"]
        validation_message = validate_fn(result)
        if validation_message is True:
            return result.strip().capitalize()
        else:
            color_print([("red", validation_message)])


# Fonction pour ajouter un joueur
def add_player():
    color_print([("cyan", "Ajoutez un nouveau joueur à la base de données.")])
    print(
        "Instructions: Entrez uniquement des lettres pour le prénom et le nom de famille."
    )
    first_name = get_valid_input("Entrez le prénom :", validate_name)
    last_name = get_valid_input("Entrez le nom de famille :", validate_name)
    print("Instructions: Entrez la date de naissance au format JJ-MM-AAAA.")
    birthdate = get_valid_input(
        "Entrez la date de naissance (DD-MM-YYYY) :", validate_date
    )

    player_controller.add_player(first_name, last_name, birthdate)
    color_print([("green", "Joueur ajouté avec succès !")])


# Fonction pour lister tous les joueurs
def list_players():
    color_print([("cyan", "Liste de tous les joueurs :")])
    players = player_controller.list_players()
    for player in players:
        print(
            f"{player['id']}: {player['first_name']} {player['last_name']} - {player['birthdate']}"
        )


# Menu de gestion des joueurs
def player_menu():
    while True:
        color_print(
            [("blue", "Menu Joueur - Gérez les joueurs dans la base de données.")]
        )
        options = [
            {"name": "Ajouter un joueur", "value": "add_player"},
            {"name": "Lister les joueurs", "value": "list_players"},
            {"name": "Retour au menu principal", "value": "return"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Sélectionnez une option :",
                "choices": options,
            }
        )["action"]
        if result == "add_player":
            add_player()
        elif result == "list_players":
            list_players()
        elif result == "return":
            break


if __name__ == "__main__":
    player_menu()
