from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import TournamentController
import re

# Initialisation du contrôleur avec le chemin vers la base de données
tournament_controller = TournamentController("data/tournament_db.json")


def validate_date(input):
    """Valider que la date est au format DD-MM-YYYY."""
    if re.match(r"^\d{2}-\d{2}-\d{4}$", input):
        return True
    return "Date must be in DD-MM-YYYY format."


def add_tournament_form():
    questions = [
        {
            "type": "input",
            "name": "name",
            "message": "Enter tournament name:",
            "validate": lambda text: True if text else "Tournament name is required",
        },
        {
            "type": "input",
            "name": "location",
            "message": "Enter location:",
            "validate": lambda text: True if text else "Location is required",
        },
        {
            "type": "input",
            "name": "date",
            "message": "Enter date (DD-MM-YYYY):",
            "validate": validate_date,
        },
    ]
    answers = prompt(questions)
    tournament_controller.add_tournament(**answers)
    color_print([("green", "Tournament added successfully!")])


def list_tournaments():
    tournaments = tournament_controller.list_tournaments()
    if tournaments:
        color_print([("cyan", "Listing all tournaments:")])
        for tournament in tournaments:
            print(
                f"{tournament['name']} at {tournament['location']} on {tournament['date']}"
            )
    else:
        color_print([("yellow", "No tournaments found.")])


def tournament_menu():
    while True:
        color_print([("blue", "\nTournament Menu")])
        options = [
            {"name": "Add Tournament", "value": "add"},
            {"name": "List Tournaments", "value": "list"},
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
            add_tournament_form()
        elif result["action"] == "list":
            list_tournaments()
        elif result["action"] == "return":
            break


if __name__ == "__main__":
    tournament_menu()
