from InquirerPy import inquirer
from InquirerPy.utils import color_print
from controllers.tournament_controller import TournamentController


def tournament_menu(controller):
    while True:
        color_print([("Yellow", "\n--- Tournament Menu ---")])
        choices = [
            {"name": "Add Tournament", "value": "add"},
            {"name": "List Tournaments", "value": "list"},
            {"name": "Return to Main Menu", "value": "return"},
        ]
        result = inquirer.select(
            message="Choose an option:",
            choices=choices,
        ).execute()

        if result == "add":
            add_tournament_form(controller)
        elif result == "list":
            list_tournaments(controller)
        elif result == "return":
            break


def add_tournament_form(controller):
    questions = [
        {"type": "input", "name": "name", "message": "Enter tournament name:"},
        {"type": "input", "name": "location", "message": "Enter location:"},
        {"type": "input", "name": "date", "message": "Enter date (DD-MM-YYYY):"},
    ]
    answers = inquirer.prompt(questions)
    controller.add_tournament(**answers)
    color_print([("Green", "Tournament added successfully!")])


def list_tournaments(controller):
    tournaments = controller.list_tournaments()
    color_print([("Blue", "Listing all tournaments...")])
    for tournament in tournaments:
        print(
            f"{tournament['name']} at {tournament['location']} on {tournament['date']}"
        )
