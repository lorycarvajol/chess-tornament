import json
import os
from models.tournament_session import TournamentSession
from controllers.tournament_controller import get_tournament_by_id
from controllers.player_controller import get_player_by_id

SESSIONS_FILE = "data/tournament_sessions.json"


def load_sessions():
    if not os.path.exists(SESSIONS_FILE):
        return []
    with open(SESSIONS_FILE, "r") as file:
        sessions_data = json.load(file)
        return [TournamentSession.from_dict(session) for session in sessions_data]


def save_sessions(sessions):
    with open(SESSIONS_FILE, "w") as file:
        json.dump([session.to_dict() for session in sessions], file, indent=4)


def add_players_to_tournament_session(tournament_id, player_ids):
    sessions = load_sessions()
    tournament = get_tournament_by_id(tournament_id)
    if not tournament:
        raise ValueError("Tournament not found")

    session = next((s for s in sessions if s.tournament_id == tournament_id), None)
    if not session:
        session = TournamentSession(
            tournament_id=tournament.id,
            tournament_name=tournament.name,
            location=tournament.location,
            date=tournament.date.strftime("%d-%m-%Y"),
        )
        sessions.append(session)

    for player_id in player_ids:
        player = get_player_by_id(player_id)
        if player:
            session.add_player(player)

    save_sessions(sessions)
    return session
