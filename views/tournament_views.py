# views/tournament_views.py

from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import (
    add_tournament,
    load_active_tournaments,
    update_tournament,
)
from datetime import datetime


def validate_date_input(date_text):
    """Validate the date input to ensure it matches the required format."""
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return "Invalid date format, use DD-MM-YYYY."  # Retournez le message d'erreur directement


def tournament_manager_menu():
    while True:
        options = [
            {"name": "Add Tournament", "value": "add"},
            {"name": "Start a Tournament", "value": "start"},
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

        if result == "add":
            add_tournament_form()
        elif result == "start":
            start_tournament_form()
        elif result == "return":
            break


def add_tournament_form():
    questions = [
        {"type": "input", "name": "name", "message": "Enter tournament name:"},
        {"type": "input", "name": "location", "message": "Enter tournament location:"},
        {
            "type": "input",
            "name": "date",
            "message": "Enter tournament date (DD-MM-YYYY):",
        },
    ]
    answers = prompt(questions)
    try:
        add_tournament(answers["name"], answers["location"], answers["date"])
        color_print(
            [("green", f"Tournament '{answers['name']}' created successfully!")]
        )
    except ValueError as e:
        color_print([("red", str(e))])


def start_tournament_form():
    tournaments = load_active_tournaments()
    if not tournaments:
        color_print([("red", "No active tournaments available.")])
        return

    tournament_choices = [{"name": t.name, "value": t.name} for t in tournaments]
    selected_tournament = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choose a tournament to start:",
            "choices": tournament_choices,
        }
    )["tournament"]

    update_tournament(selected_tournament)
    color_print([("green", f"Tournament {selected_tournament} started!")])
