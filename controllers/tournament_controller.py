import json
import os
from models.tournament import Tournament

TOURNAMENTS_FILE = "data/tournaments.json"


def load_tournaments():
    # Assurer la création du dossier data et du fichier JSON s'ils n'existent pas
    os.makedirs(os.path.dirname(TOURNAMENTS_FILE), exist_ok=True)
    if not os.path.exists(TOURNAMENTS_FILE):
        with open(TOURNAMENTS_FILE, "w") as f:
            f.write("[]")  # Écrire un tableau vide en JSON

    with open(TOURNAMENTS_FILE, "r") as file:
        data = file.read()
        if not data:  # Vérifier si le fichier est vide
            return []
        return [Tournament(**tournament) for tournament in json.loads(data)]


def save_tournaments(tournaments):
    with open(TOURNAMENTS_FILE, "w") as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)


def add_tournament(name, location, date):
    tournaments = load_tournaments()
    tournament = Tournament(name, location, date)
    tournaments.append(tournament)
    save_tournaments(tournaments)
