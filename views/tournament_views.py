from controllers.player_controller import load_all_players
from InquirerPy import prompt
from colorama import Fore, Style
import os
import json


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

    # Obtenez les informations de base du tournoi
    answers = prompt(questions)

    # Récupérez tous les joueurs depuis le fichier JSON
    players = load_all_players()
    if not players:
        print(
            Fore.YELLOW
            + "No players found. Please add players first."
            + Style.RESET_ALL
        )
        return

    # Demandez la sélection des joueurs pour le tournoi
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

    # Vérifiez si des joueurs ont été sélectionnés
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
