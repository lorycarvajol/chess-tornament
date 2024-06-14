from datetime import datetime
from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.player_controller import PlayerController
import re

# Initialisation du contrôleur des joueurs
player_controller = PlayerController("data/players.json")


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
        datetime.strptime(input_date, "%d-%m-%YYYY")
    except ValueError:
        return "Invalid date. Please ensure the day, month, and year are correct."
    return True


def add_player():
    color_print([("cyan", "Add a new player to the database.")])
    questions = [
        {"type": "input", "name": "first_name", "message": "Enter first name:"},
        {"type": "input", "name": "last_name", "message": "Enter last name:"},
        {
            "type": "input",
            "name": "birthdate",
            "message": "Enter birthdate (DD-MM-YYYY):",
            "validate": validate_date,
        },
    ]
    answers = prompt(questions)
    player_controller.add_player(
        answers["first_name"], answers["last_name"], answers["birthdate"]
    )
    color_print([("green", "Player added successfully!")])


def list_players():
    color_print([("cyan", "Listing all players:")])
    players = player_controller.list_players()
    for player in players:
        print(
            f"{player['id']}: {player['first_name']} {player['last_name']} - {player['birthdate']}"
        )


def player_menu():
    while True:
        color_print([("blue", "Player Menu - Manage players in the database.")])
        options = [
            {"name": "Add Player", "value": "add_player"},
            {"name": "List Players", "value": "list_players"},
            {"name": "Return to Main Menu", "value": "return"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Select an option:",
                "choices": options,
            }
        )["action"]
        if result == "add_player":
            add_player()
        elif result == "list_players":
            list_players()
        elif result == "return":
            break
