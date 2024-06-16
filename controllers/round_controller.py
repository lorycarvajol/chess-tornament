from datetime import datetime
from models.round import Round
from models.match import Match


def create_round(tournament, name):
    """
    Crée un nouvel objet Round et l'ajoute au tournoi.

    Args:
        tournament: L'objet tournoi auquel ajouter la nouvelle manche.
        name: Le nom de la nouvelle manche.
    """
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    round_obj = Round(name, start_time)
    tournament.rounds.append(round_obj)
    print(f"Round '{name}' créé avec succès et démarré à {start_time}.")


def create_match(tournament, player1, player2):
    """
    Crée un nouvel objet Match et l'ajoute à la manche actuelle du tournoi.

    Args:
        tournament: L'objet tournoi auquel ajouter le nouveau match.
        player1: Le premier joueur du match.
        player2: Le deuxième joueur du match.
    """
    current_round = tournament.rounds[tournament.current_round]
    match = Match(player1, player2)
    current_round.matches.append(match)
    print(
        f"Match créé entre {player1.name} et {player2.name} dans la manche '{current_round.name}'."
    )


def update_match_score(tournament, match_index, player_index, score):
    """
    Met à jour le score d'un joueur dans un match donné.

    Args:
        tournament: L'objet tournoi contenant le match.
        match_index: L'index du match dans la manche actuelle.
        player_index: L'index du joueur (0 ou 1) dans le match.
        score: Le nouveau score du joueur.
    """
    current_round = tournament.rounds[tournament.current_round]
    match = current_round.matches[match_index]
    player, _ = match.players[player_index]
    match.players[player_index] = (player, score)
    print(
        f"Score de {player.name} mis à jour à {score} dans le match {match_index + 1} de la manche '{current_round.name}'."
    )


def end_round(tournament):
    """
    Termine la manche actuelle du tournoi et passe à la suivante.

    Args:
        tournament: L'objet tournoi contenant la manche actuelle.
    """
    current_round = tournament.rounds[tournament.current_round]
    current_round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Manche '{current_round.name}' terminée à {current_round.end_time}.")
    tournament.current_round += 1
    if tournament.current_round < len(tournament.rounds):
        print(
            f"La prochaine manche '{tournament.rounds[tournament.current_round].name}' commencera maintenant."
        )
    else:
        print("Toutes les manches du tournoi sont terminées.")
