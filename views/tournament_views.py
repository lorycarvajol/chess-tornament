# views/tournament_views.py

from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import (
    add_tournament,
    load_active_tournaments,
    get_tournament_by_name,
    update_tournament,
)
from controllers.player_controller import load_all_players, get_player_by_id
from controllers.tournament_session_controller import start_tournament_session

from datetime import datetime


def validate_date_input(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return "Invalid date format, use DD-MM-YYYY."


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
            "validate": validate_date_input,
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

    tournament_choices = [{"name": t.name, "value": t} for t in tournaments]
    selected_tournament = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choose a tournament to start:",
            "choices": tournament_choices,
        }
    )["tournament"]

    tournament = get_tournament_by_name(selected_tournament)
    players = load_all_players()
    player_choices = [
        {"name": f"{p.first_name} {p.last_name}", "value": p.id} for p in players
    ]
    selected_player_ids = prompt(
        {
            "type": "checkbox",
            "name": "players",
            "message": "Select players for this tournament:",
            "choices": player_choices,
        }
    )["players"]

    if not selected_player_ids:
        color_print([("yellow", "No players selected for the tournament.")])
        return

    try:
        session = start_tournament_session(tournament.name, selected_player_ids)
        color_print(
            [("green", f"Tournament {tournament.name} started with selected players!")]
        )
    except Exception as e:
        color_print([("red", str(e))])
