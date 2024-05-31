# controllers/tournament_session_controller.py
import json
import os
from models.tournament_session import TournamentSession
from controllers.tournament_controller import get_tournament_by_name
from controllers.player_controller import get_player_by_id

SESSIONS_FILE = "data/sessions.json"


def load_sessions():

    if not os.path.exists(SESSIONS_FILE):
        return []
    with open(SESSIONS_FILE, "r") as file:
        sessions_data = json.load(file)
        return [TournamentSession.from_dict(sd) for sd in sessions_data]


def save_sessions(sessions):

    with open(SESSIONS_FILE, "w") as file:
        json.dump([session.to_dict() for session in sessions], file, indent=4)


def start_tournament_session(tournament_name, player_ids):

    tournament = get_tournament_by_name(tournament_name)
    if not tournament:
        raise ValueError("Tournament not found")

    players = [get_player_by_id(pid) for pid in player_ids if get_player_by_id(pid)]
    if not players:
        raise ValueError("No valid players found with the provided IDs")

    new_session = TournamentSession(tournament, players)
    sessions = load_sessions()
    sessions.append(new_session)
    save_sessions(sessions)
    return new_session


def add_match_to_session(session_id, player1_id, player2_id, winner_id):

    sessions = load_sessions()
    session = next((s for s in sessions if s.id == session_id), None)
    if not session:
        raise ValueError("Session not found")

    player1 = get_player_by_id(player1_id)
    player2 = get_player_by_id(player2_id)
    winner = get_player_by_id(winner_id)
    if not all([player1, player2, winner]):
        raise ValueError("One or more players not found")

    session.add_match_result(player1, player2, winner)
    save_sessions(sessions)
