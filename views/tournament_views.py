# views/tournament_views.py

from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import (
    load_active_tournaments,
    get_tournament_by_name,
    update_tournament,
    add_tournament,
)
from controllers.player_controller import get_player_by_id, load_all_players


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

    tournament_choices = [{"name": t.name, "value": t} for t in tournaments]
    selected_tournament = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Choose a tournament to start:",
            "choices": tournament_choices,
        }
    )["tournament"]

    players = load_all_players()
    if not players:
        color_print([("yellow", "No players available to add to the tournament.")])
        return

    player_choices = [
        {"name": f"{player.first_name} {player.last_name}", "value": player.id}
        for player in players
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

    # Mise à jour des joueurs dans le tournoi
    selected_tournament.players.extend(selected_player_ids)
    update_tournament(selected_tournament)

    color_print(
        [
            (
                "green",
                f"Tournament {selected_tournament.name} updated with selected players!",
            )
        ]
    )
