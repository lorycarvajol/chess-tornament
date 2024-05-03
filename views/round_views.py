from controllers.round_controller import create_round, create_match, update_match_score, end_round

def create_new_round(tournament):
    name = input("Enter round name: ")
    create_round(tournament, name)

def add_match_to_round(tournament, players):
    player1_id = int(input("Enter player 1 ID: "))
    player2_id = int(input("Enter player 2 ID: "))
    player1 = players[player1_id]
    player2 = players[player2_id]
    create_match(tournament, player1, player2)

def update_match_result(tournament):
    match_index = int(input("Enter match index: "))
    player_index = int(input("Enter player index (0 or 1): "))
    score = float(input("Enter player's score: "))
    update_match_score(tournament, match_index, player_index, score)

def mark_round_as_completed(tournament):
    end_round(tournament)
