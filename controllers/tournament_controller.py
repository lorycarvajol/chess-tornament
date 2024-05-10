import os
import json
from colorama import Fore, Style
from InquirerPy import prompt

TOURNAMENTS_FILE = "data/tournaments.json"


def add_tournament_form():
    """Ajouter un nouveau tournoi, y compris la sélection des joueurs participants."""
    questions = [
        {"type": "input", "name": "name", "message": "Tournament name:"},
        {"type": "input", "name": "location", "message": "Location:"},
        {
            "type": "input",
            "name": "date",
            "message": "Date (DD-MM-YYYY):",
            "validate": lambda text: "Date is required" if not text else True,
        },
    ]

    answers = prompt(questions)

    # Charger la liste de joueurs depuis un fichier existant
    players_file = "data/players.json"
    if os.path.exists(players_file):
        with open(players_file, "r") as file:
            players = json.load(file)
    else:
        players = []

    if not players:
        print(
            Fore.YELLOW
            + "No players found. Please add players first."
            + Style.RESET_ALL
        )
        return

    # Demander la sélection des joueurs pour le tournoi
    player_choices = [
        {"name": f"{p['first_name']} {p['last_name']}", "value": p} for p in players
    ]
    selected_prompt = prompt(
        {
            "type": "checkbox",
            "name": "players",
            "message": "Select players for this tournament:",
            "choices": player_choices,
        }
    )

    selected_players = selected_prompt["players"]

    if not selected_players:
        print(Fore.YELLOW + "No players selected for the tournament." + Style.RESET_ALL)
        return

    # Créez un dictionnaire pour représenter le tournoi et les joueurs sélectionnés
    tournament = {
        "name": answers["name"],
        "location": answers["location"],
        "date": answers["date"],
        "players": selected_players,
    }

    # Enregistrez le tournoi dans un fichier JSON
    os.makedirs("data/tournaments", exist_ok=True)
    file_name = f"data/tournaments/{tournament['name']}.json"
    with open(file_name, "w") as file:
        json.dump(tournament, file, indent=4)

    print(
        Fore.GREEN
        + f"Tournament '{tournament['name']}' created successfully!"
        + Style.RESET_ALL
    )
