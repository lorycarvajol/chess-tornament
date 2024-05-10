import json
import os
from colorama import Fore, Style
from models.player import Player
from InquirerPy import prompt
from datetime import datetime

# Chemin vers le fichier JSON contenant tous les joueurs
PLAYERS_FILE = "data/players.json"


def validate_date(date_str):
    """Valider le format de la date."""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def load_all_players():
    """Charger tous les joueurs depuis un fichier JSON."""
    if os.path.exists(PLAYERS_FILE):
        with open(PLAYERS_FILE, "r") as file:
            return json.load(file)
    return []


def save_all_players(players):
    """Enregistrer tous les joueurs dans un fichier JSON."""
    with open(PLAYERS_FILE, "w") as file:
        json.dump(players, file, indent=4)


def add_player_form():
    """Ajouter un nouveau joueur et l'enregistrer dans le fichier JSON."""
    os.makedirs("data", exist_ok=True)

    questions = [
        {"type": "input", "name": "first_name", "message": "First name:"},
        {"type": "input", "name": "last_name", "message": "Last name:"},
        {
            "type": "input",
            "name": "birthdate",
            "message": "Birthdate (DD-MM-YYYY):",
            "validate": lambda text: (
                "Invalid date format, use DD-MM-YYYY."
                if not validate_date(text)
                else True
            ),
        },
    ]
    answers = prompt(questions)

    # Créez un nouvel objet Player
    new_player = Player(
        answers["first_name"], answers["last_name"], answers["birthdate"]
    )

    # Chargez tous les joueurs existants
    players = load_all_players()

    # Ajouter le nouveau joueur sous forme de dictionnaire
    players.append(new_player.__dict__)

    # Enregistrez tous les joueurs dans le fichier JSON
    save_all_players(players)

    print(
        Fore.GREEN
        + f"Player '{answers['first_name']} {answers['last_name']}' added successfully!"
        + Style.RESET_ALL
    )


def list_all_players():
    """Lister tous les joueurs en affichant leurs détails."""
    os.makedirs("data", exist_ok=True)

    print(Fore.CYAN + "\nList of Players:" + Style.RESET_ALL)

    # Charger tous les joueurs depuis le fichier
    players = load_all_players()

    if players:
        for player in players:
            # Vérifier la présence des clés nécessaires
            if all(key in player for key in ["first_name", "last_name", "birthdate"]):
                print(
                    f"{player['first_name']} {player['last_name']}, born on {player['birthdate']}"
                )
            else:
                print(
                    Fore.RED
                    + f"Incomplete data found: {player}. Skipping."
                    + Style.RESET_ALL
                )
    else:
        print(Fore.YELLOW + "No players found." + Style.RESET_ALL)
