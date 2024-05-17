# views/tournament_views.py

from controllers.tournament_controller import (
    load_active_tournaments,
    play_tournament,
    add_tournament,
)
from controllers.player_controller import load_all_players
from InquirerPy import prompt
from InquirerPy.utils import color_print


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
    add_tournament(answers["name"], answers["location"], answers["date"])
    color_print([("green", f"Tournament '{answers['name']}' created successfully!")])


def start_tournament_form():
    tournaments = load_active_tournaments()
    if not tournaments:
        color_print([("red", "No active tournaments available.")])
        return

    tournament_choices = [{"name": t.name, "value": t.name} for t in tournaments]
    tournament_name = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choose a tournament to start:",
            "choices": tournament_choices,
        }
    )["tournament"]

    tournament = play_tournament(tournament_name)
    color_print([("cyan", f"Starting tournament: {tournament.name}")])

    # Continue with player selection
    players = load_all_players()
    player_choices = [
        {"name": f"{p.first_name} {p.last_name}", "value": p} for p in players
    ]
    selected_players = prompt(
        {
            "type": "checkbox",
            "name": "players",
            "message": "Select players for this tournament:",
            "choices": player_choices,
        }
    )["players"]

    # Here, you would ideally add the selected players to the tournament and save it
    color_print(
        [
            (
                "green",
                f"Players selected for the tournament: {', '.join([p['first_name'] + ' ' + p['last_name'] for p in selected_players])}",
            )
        ]
    )
