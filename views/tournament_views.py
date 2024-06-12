from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import (
    load_active_tournaments,
    get_tournament_by_id,
    add_tournament,
)
from controllers.player_controller import load_all_players
from controllers.tournament_session_controller import add_players_to_tournament_session
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
            {"name": "Add Tournament", "value": "add_tournament"},
            {"name": "Play Tournament", "value": "play_tournament"},
            {"name": "Add Players to Tournament", "value": "add_players_to_tournament"},
            {"name": "List Tournaments", "value": "list_tournaments"},
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

        if result == "add_tournament":
            add_tournament_form()
        elif result == "play_tournament":
            start_tournament_form()
        elif result == "add_players_to_tournament":
            add_players_to_tournament_form()
        elif result == "list_tournaments":
            list_tournaments()
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


def add_players_to_tournament_form():
    tournaments = load_active_tournaments()
    if not tournaments:
        color_print([("red", "No active tournaments available.")])
        return

    tournament_choices = [{"name": t.name, "value": t.id} for t in tournaments]
    selected_tournament_id = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choose a tournament to add players:",
            "choices": tournament_choices,
        }
    )["tournament"]

    players = load_all_players()
    if not players:
        color_print([("yellow", "No players available.")])
        return

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

    session = add_players_to_tournament_session(
        selected_tournament_id, selected_player_ids
    )
    color_print(
        [
            (
                "green",
                f"Players added to tournament session with ID {session.tournament_id}.",
            )
        ]
    )


def list_tournaments():
    tournaments = load_active_tournaments()
    if not tournaments:
        color_print([("yellow", "No active tournaments found.")])
        return

    color_print([("cyan", "Active Tournaments:")])
    for tournament in tournaments:
        color_print(
            [
                (
                    "cyan",
                    f"{tournament.id}: {tournament.name} - {tournament.location} on {tournament.date.strftime('%d-%m-%Y')}",
                )
            ]
        )
