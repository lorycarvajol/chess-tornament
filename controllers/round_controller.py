from datetime import datetime
from models.round import Round
from models.match import Match

def create_round(tournament, name):
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    round_obj = Round(name, start_time)
    tournament.rounds.append(round_obj)

def create_match(tournament, player1, player2):
    current_round = tournament.rounds[tournament.current_round]
    match = Match(player1, player2)
    current_round.matches.append(match)

def update_match_score(tournament, match_index, player_index, score):
    current_round = tournament.rounds[tournament.current_round]
    match = current_round.matches[match_index]
    player, _ = match.players[player_index]
    match.players[player_index] = (player, score)

def end_round(tournament):
    current_round = tournament.rounds[tournament.current_round]
    current_round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tournament.current_round += 1
