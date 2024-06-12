import json
import os
from models.tournament import Tournament

TOURNAMENTS_FILE = "data/tournaments.json"


def load_tournaments():
    if not os.path.exists(TOURNAMENTS_FILE):
        return []
    with open(TOURNAMENTS_FILE, "r") as file:
        return [Tournament.from_dict(data) for data in json.load(file)]


def save_tournaments(tournaments):
    with open(TOURNAMENTS_FILE, "w") as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)


def add_tournament(name, location, date):
    tournaments = load_tournaments()
    new_tournament = Tournament(name, location, date)
    tournaments.append(new_tournament)
    save_tournaments(tournaments)


def update_tournament(updated_tournament):
    tournaments = load_tournaments()
    for index, tournament in enumerate(tournaments):
        if tournament.id == updated_tournament.id:
            tournaments[index] = updated_tournament
            break
    save_tournaments(tournaments)


def get_tournament_by_id(tournament_id):
    tournaments = load_tournaments()
    return next((t for t in tournaments if t.id == tournament_id), None)


def load_active_tournaments():
    return [
        tournament for tournament in load_tournaments() if not tournament.is_finished
    ]
