import json
import os
from models.tournament import Tournament

TOURNAMENTS_FILE = "data/tournaments.json"


def load_tournaments():
    os.makedirs(os.path.dirname(TOURNAMENTS_FILE), exist_ok=True)
    if not os.path.exists(TOURNAMENTS_FILE):
        with open(TOURNAMENTS_FILE, "w") as f:
            f.write("[]")

    with open(TOURNAMENTS_FILE, "r") as file:
        data = file.read()
        if not data:
            return []
        return [Tournament.from_dict(tournament) for tournament in json.loads(data)]


def save_tournaments(tournaments):
    with open(TOURNAMENTS_FILE, "w") as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)


def add_tournament(name, location, date):
    tournaments = load_tournaments()
    tournament = Tournament(name, location, date)
    tournaments.append(tournament)
    save_tournaments(tournaments)


def load_active_tournaments():
    """Charge tous les tournois qui ne sont pas encore terminés."""
    tournaments = load_tournaments()
    # Assumer que Tournament a un attribut `is_finished` pour vérifier l'état
    return [t for t in tournaments if not t.is_finished]


def play_tournament(tournament_name):
    """Sélectionner et préparer un tournoi à jouer."""
    tournaments = load_tournaments()
    tournament = next((t for t in tournaments if t.name == tournament_name), None)
    if not tournament:
        raise ValueError("Tournament not found")
    # Cette fonction pourrait être étendue pour inclure la sélection des joueurs
    return tournament


def start_tournament(tournament_name):
    tournaments = load_tournaments()
    tournament = next((t for t in tournaments if t.name == tournament_name), None)
    if tournament is None:
        raise ValueError("Tournament not found")
    if tournament.is_finished:
        raise ValueError("Tournament already completed")
    # Here you would initiate the tournament play logic, which would update the tournament's state
    save_tournaments(tournaments)
    return tournament
