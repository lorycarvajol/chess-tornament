from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.player_controller import PlayerController
import re

# Initialisation du contrôleur
player_controller = PlayerController("data/player_db.json")


def validate_name(input):
    """Valider que le nom contient uniquement des lettres."""
    if re.match(r"^[A-Za-z\s]+$", input):
        return True
    return "Names can only contain letters."


def validate_date(input):
    """Valider que la date est au format DD-MM-YYYY."""
    if re.match(r"^\d{2}-\d{2}-\d{4}$", input):
        return True
    return "Date must be in DD-MM-YYYY format."


def validate_national_id(input):
    """Valider que l'ID est un numéro."""
    if re.match(r"^\d+$", input):
        return True
    return "National ID must be numeric."


def add_player_form():
    questions = [
        {
            "type": "input",
            "name": "first_name",
            "message": "Enter player's first name:",
            "validate": validate_name,
        },
        {
            "type": "input",
            "name": "last_name",
            "message": "Enter player's last name:",
            "validate": validate_name,
        },
        {
            "type": "input",
            "name": "date_of_birth",
            "message": "Enter player's date of birth (DD-MM-YYYY):",
            "validate": validate_date,
        },
        {
            "type": "input",
            "name": "national_id",
            "message": "Enter player's national ID:",
            "validate": validate_national_id,
        },
    ]
    answers = prompt(questions)
    try:
        player_controller.add_player(**answers)
        color_print([("green", "Player added successfully!")])
    except Exception as e:
        color_print([("red", str(e))])


def list_players():
    players = player_controller.list_players()
    if players:
        color_print([("cyan", "Listing all players:")])
        for player in players:
            print(
                f"{player['first_name']} {player['last_name']} - DOB: {player['date_of_birth']} - ID: {player['national_id']}"
            )
    else:
        color_print([("yellow", "No players found.")])


def player_menu():
    while True:
        color_print([("blue", "\nPlayer Menu")])
        options = [
            {"name": "Add Player", "value": "add"},
            {"name": "List Players", "value": "list"},
            {"name": "Return to Main Menu", "value": "return"},
        ]
        result = prompt(
            {
                "type": "list",
                "name": "action",
                "message": "Select an option:",
                "choices": options,
            }
        )

        if result["action"] == "add":
            add_player_form()
        elif result["action"] == "list":
            list_players()
        elif result["action"] == "return":
            break


if __name__ == "__main__":
    player_menu()
