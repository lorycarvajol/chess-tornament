# controllers/player_controller.py

import json
import os
from models.player import Player
from InquirerPy import prompt
from InquirerPy.utils import color_print
from datetime import datetime

PLAYERS_FILE = "data/players.json"


def load_all_players():
    """Charge tous les joueurs à partir du fichier JSON."""
    try:
        with open(PLAYERS_FILE, "r") as file:
            players_data = json.load(file)
            return [Player.from_dict(player) for player in players_data]
    except FileNotFoundError:
        # Créer le fichier s'il n'existe pas et retourner une liste vide
        with open(PLAYERS_FILE, "w") as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError:
        # Gérer le cas où le fichier est vide ou corrompu
        return []


def save_all_players(players):
    with open(PLAYERS_FILE, "w") as file:
        json.dump([player.to_dict() for player in players], file, indent=4)


def get_next_player_id():
    players = load_all_players()
    return max((player.id for player in players), default=0) + 1


def add_player_form():
    """Form for adding a new player and saving it in the JSON file."""
    questions = [
        {"type": "input", "name": "first_name", "message": "Prénom :"},
        {"type": "input", "name": "last_name", "message": "Nom :"},
        {
            "type": "input",
            "name": "birthdate",
            "message": "Date de naissance (JJ-MM-AAAA) :",
            "validate": lambda text: (
                "Format de date invalide, utilisez JJ-MM-AAAA."
                if not validate_date(text)
                else True
            ),
        },
    ]
    answers = prompt(questions)
    new_player = Player(
        answers["first_name"],
        answers["last_name"],
        answers["birthdate"],
        get_next_player_id(),
    )
    players = load_all_players()
    players.append(new_player)
    save_all_players(players)
    color_print(
        [
            (
                "green",
                f"Joueur '{answers['first_name']} {answers['last_name']}' ajouté avec succès!",
            )
        ]
    )


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return "Format de date invalide, utilisez JJ-MM-AAAA."


def list_all_players():
    """List all players and display their details."""
    players = load_all_players()
    if players:
        for player in players:
            color_print(
                [
                    (
                        "cyan",
                        f"{player.first_name} {player.last_name}, né(e) le {player.birthdate}",
                    )
                ]
            )
    else:
        color_print([("yellow", "Aucun joueur trouvé.")])


def get_player_by_id(player_id):
    """Retrieve a player by their ID."""
    players = (
        load_all_players()
    )  # Assuming this function returns a list of Player instances
    for player in players:
        if player.id == player_id:
            return player
    return None  # Return None if no player is found with the given ID
