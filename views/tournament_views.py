from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.tournament_session_controller import TournamentSessionController
from controllers.tournament_round_controller import TournamentRoundController
from datetime import datetime
import re

# Initialisation des contrôleurs
tournament_controller = TournamentController("data/tournaments.json")
player_controller = PlayerController("data/players.json")
session_controller = TournamentSessionController("data/tournament_sessions.json")
round_controller = TournamentRoundController("data")


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


def add_tournament():
    color_print([("cyan", "Add a new tournament to the database.")])
    questions = [
        {"type": "input", "name": "name", "message": "Enter tournament name:"},
        {"type": "input", "name": "location", "message": "Enter location:"},
        {
            "type": "input",
            "name": "date",
            "message": "Enter date (DD-MM-YYYY):",
            "validate": validate_date,
        },
    ]
    answers = prompt(questions)
    tournament_controller.add_tournament(
        answers["name"], answers["location"], answers["date"]
    )
    color_print([("green", "Tournament added successfully!")])


def list_tournaments():
    color_print([("cyan", "Listing all tournaments:")])
    tournaments = tournament_controller.list_tournaments()
    for tournament in tournaments:
        print(
            f"{tournament['id']}: {tournament['name']} - {tournament['location']} on {tournament['date']}"
        )


def add_players_to_tournament():
    color_print([("cyan", "Add players to an existing tournament.")])
    tournaments = tournament_controller.list_tournaments()
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
    session = session_controller.start_tournament_session(
        selected_tournament_id, selected_player_ids
    )
    color_print(
        [("green", f"Players added to the tournament session with ID {session['id']}.")]
    )
    if prompt(
        {
            "type": "confirm",
            "name": "start_tournament",
            "message": "Do you want to start the tournament now?",
            "default": True,
        }
    )["start_tournament"]:
        player_scores, rounds = round_controller.start_tournament(
            session["id"], selected_player_ids
        )
        color_print(
            [("green", "Tournament started! Here are the scores after each round:")]
        )
        for round_info in rounds:
            print(f"Round {round_info['round_number']}:")
            for result in round_info["results"]:
                print(
                    f"  Match: {result['player1']} vs {result['player2']} - Winner: {result['winner']}"
                )
        print("Final Scores:")
        for player_id, score in player_scores.items():
            player_name = round_controller.get_player_name(player_id, players)
            print(f"  {player_name}: {score} points")


def tournament_menu():
    while True:
        color_print([("blue", "Tournament Menu - Manage tournaments in the database.")])
        options = [
            {"name": "Add Tournament", "value": "add_tournament"},
            {"name": "List Tournaments", "value": "list_tournaments"},
            {"name": "Add Players to Tournament", "value": "add_players"},
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
            add_tournament()
        elif result == "list_tournaments":
            list_tournaments()
        elif result == "add_players":
            add_players_to_tournament()
        elif result == "return":
            break
