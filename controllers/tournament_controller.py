# controllers/tournament_controller.py
import json
import os
from controllers.player_controller import get_player_by_id, load_all_players
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
        if tournament.name == updated_tournament.name:
            tournaments[index] = updated_tournament
            break
    save_tournaments(tournaments)


def get_tournament_by_name(name):
    tournaments = load_tournaments()
    return next((t for t in tournaments if t.name == name), None)


def load_active_tournaments():
    """Charge tous les tournois et filtre ceux qui ne sont pas terminés."""
    return [
        tournament for tournament in load_tournaments() if not tournament.is_finished
    ]


def play_tournament(tournament_name, player_ids):
    tournaments = load_tournaments()
    tournament = next((t for t in tournaments if t.name == tournament_name), None)
    if not tournament:
        raise ValueError("Tournament not found")

    # Intégration des joueurs dans le tournoi
    tournament.players = [get_player_by_id(pid) for pid in player_ids]
    update_tournament(tournament)
    return tournament


def get_player_by_id(player_id):
    players = load_all_players()
    return next((player for player in players if player.id == player_id), None)


# Assurez-vous que cette fonction est correctement définie dans votre controller
def update_tournament(updated_tournament):
    tournaments = load_tournaments()
    found = False
    for index, t in enumerate(tournaments):
        if t.name == updated_tournament.name:
            tournaments[index] = updated_tournament
            found = True
            break
    if not found:
        tournaments.append(updated_tournament)
    save_tournaments(tournaments)
