import json
import os
from models.player import Player
from InquirerPy import prompt
from InquirerPy.utils import color_print
from datetime import datetime

PLAYERS_FILE = "data/players.json"


def load_all_players():
    if not os.path.exists(PLAYERS_FILE):
        return []
    with open(PLAYERS_FILE, "r") as file:
        players_data = json.load(file)
        return [Player.from_dict(player) for player in players_data]


def save_all_players(players):
    with open(PLAYERS_FILE, "w") as file:
        json.dump([player.to_dict() for player in players], file, indent=4)


def get_player_by_id(player_id):
    players = load_all_players()
    return next((player for player in players if player.id == player_id), None)


def add_player_form():
    questions = [
        {"type": "input", "name": "first_name", "message": "First name:"},
        {"type": "input", "name": "last_name", "message": "Last name:"},
        {
            "type": "input",
            "name": "birthdate",
            "message": "Birthdate (DD-MM-YYYY):",
            "validate": lambda text: validate_date(text),
        },
    ]
    answers = prompt(questions)
    players = load_all_players()
    new_id = max((player.id for player in players), default=0) + 1
    new_player = Player(
        first_name=answers["first_name"],
        last_name=answers["last_name"],
        birthdate=answers["birthdate"],
        player_id=new_id,
    )
    players.append(new_player)
    save_all_players(players)
    color_print(
        [
            (
                "green",
                f"Player '{new_player.first_name} {new_player.last_name}' added successfully!",
            )
        ]
    )


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return "Invalid date format, use DD-MM-YYYY."


def list_all_players():
    players = load_all_players()
    if not players:
        color_print([("yellow", "No players found.")])
        return

    color_print([("cyan", "List of Players:")])
    for player in players:
        color_print(
            [
                (
                    "cyan",
                    f"{player.id}: {player.first_name} {player.last_name}, born on {player.birthdate}",
                )
            ]
        )
