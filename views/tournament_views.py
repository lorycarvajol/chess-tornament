from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import TournamentController
from controllers.tournament_session_controller import TournamentSessionController
from controllers.player_controller import PlayerController
import re
from datetime import datetime

tournament_controller = TournamentController("data/tournaments.json")
player_controller = PlayerController("data/players.json")
session_controller = TournamentSessionController("data")


def validate_date(input_date):
    """Validate that the date is in DD-MM-YYYY format and is a valid date."""
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", input_date):
        return "Date must be in DD-MM-YYYY format."
    try:
        datetime.strptime(input_date, "%d-%m-%Y")
    except ValueError:
        return "Invalid date. Please ensure the day, month, and year are correct."
    return True


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
                f"{tournament['id']}: {tournament['name']} at {tournament['location']} on {tournament['date']}"
            )
    else:
        color_print([("yellow", "No tournaments found.")])


def add_players_to_tournament():
    tournaments = tournament_controller.list_tournaments()
    if not tournaments:
        color_print([("red", "No tournaments available.")])
        return

    tournament_choices = [
        {"name": f"{t['id']}: {t['name']}", "value": t["id"]} for t in tournaments
    ]
    selected_tournament_id = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choose a tournament to add players:",
            "choices": tournament_choices,
        }
    )["tournament"]

    players = player_controller.list_players()
    if not players:
        color_print([("yellow", "No players available.")])
        return

    player_choices = [
        {"name": f"{p['first_name']} {p['last_name']}", "value": p["id"]}
        for p in players
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

    selected_tournament = next(
        t for t in tournaments if t["id"] == selected_tournament_id
    )
    selected_players = [p for p in players if p["id"] in selected_player_ids]
    session = session_controller.start_tournament_session(
        selected_tournament, selected_players
    )
    color_print([("green", f"Tournament session started with ID {session['id']}")])


def tournament_menu():
    while True:
        color_print(
            [("blue", "\nTournament Menu - Manage tournaments in the database.")]
        )
        options = [
            {"name": "Add Tournament", "value": "add"},
            {"name": "Play Tournament", "value": "play"},
            {"name": "Add Players to Tournament", "value": "add_players"},
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
        )["action"]

        if result == "add":
            add_tournament_form()
        elif result == "play":
            add_players_to_tournament()  # This method includes starting the tournament
        elif result == "add_players":
            add_players_to_tournament()
        elif result == "list":
            list_tournaments()
        elif result == "return":
            break
