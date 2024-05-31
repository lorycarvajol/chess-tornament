# controllers/tournament_controller.py
import json
import os
from models.tournament import Tournament
from controllers.player_controller import get_player_by_id, load_all_players

TOURNAMENTS_FILE = "data/tournaments.json"


def load_tournaments():
    if not os.path.exists(TOURNAMENTS_FILE):
        return []
    with open(TOURNAMENTS_FILE, "r") as file:
        return [Tournament.from_dict(data) for data in json.load(file)]


def save_tournaments(tournaments):
    with open(TOURNAMENTS_FILE, "w") as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)


def get_next_tournament_id():
    tournaments = load_tournaments()
    if tournaments:
        return max(tournament.id for tournament in tournaments) + 1
    return 1


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


def get_tournament_by_name(name):
    tournaments = load_tournaments()
    return next((t for t in tournaments if t.name == name), None)


def get_tournament_by_id(tournament_id):
    tournaments = load_tournaments()
    return next((t for t in tournaments if t.id == tournament_id), None)


def load_active_tournaments():
    return [
        tournament for tournament in load_tournaments() if not tournament.is_finished
    ]


def play_tournament(tournament_name, player_ids):
    # Récupérer le tournoi par son nom
    tournament = get_tournament_by_name(tournament_name)
    if not tournament:
        raise ValueError(f"Tournament '{tournament_name}' not found")

    players = [get_player_by_id(pid) for pid in player_ids]
    valid_players = [player for player in players if player]

    if not valid_players:
        raise Exception("No valid players found with the provided IDs")

    tournament.players.extend(valid_players)
    update_tournament(tournament)

    return tournament


def get_player_by_id(player_id):
    players = load_all_players()
    return next((player for player in players if player.id == player_id), None)
