from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from models.match import Match
from models.round import Round

# Initialisation des contrôleurs
tournament_controller = TournamentController()
player_controller = PlayerController()


def add_tournament_form():
    """Ajouter un nouveau tournoi, y compris la sélection des joueurs participants."""
    questions = [
        {
            "type": "input",
            "name": "name",
            "message": "Enter tournament name:",
            "validate": lambda text: (
                "Tournament name is required" if not text else True
            ),
        },
        {
            "type": "input",
            "name": "location",
            "message": "Enter location:",
            "validate": lambda text: "Location is required" if not text else True,
        },
        {
            "type": "input",
            "name": "date",
            "message": "Enter date (DD-MM-YYYY):",
            "validate": lambda text: "Date is required" if not text else True,
        },
    ]

    # Obtenir les informations de base du tournoi
    answers = prompt(questions)

    # Récupérer la liste des joueurs disponibles
    players = player_controller.get_all_players()
    if not players:
        color_print([("yellow", "No players found. Please add players first.")])
        return

    # Demander la sélection des joueurs pour le tournoi
    player_choices = [
        {"name": f"{p.first_name} {p.last_name}", "value": p} for p in players
    ]
    selected_prompt = prompt(
        {
            "type": "checkbox",
            "name": "players",
            "message": "Select players for this tournament:",
            "choices": player_choices,
        }
    )

    selected_players = selected_prompt["players"]

    # Débogage : Vérifier les joueurs sélectionnés
    print(f"Selected players (debug): {selected_players}")

    if not selected_players:
        color_print([("yellow", "No players selected for the tournament.")])
        return

    # Créer un tournoi avec les joueurs sélectionnés
    try:
        tournament = tournament_controller.create_tournament(
            name=answers["name"],
            location=answers["location"],
            date=answers["date"],
            players=selected_players,
        )
        color_print(
            [("green", f"Tournament '{tournament.name}' created successfully!")]
        )
    except ValueError as e:
        color_print([("red", f"Error: {str(e)}")])


def list_tournaments():
    """Lister tous les tournois enregistrés."""
    tournaments = tournament_controller.tournaments
    if tournaments:
        color_print([("cyan", "\nList of Tournaments:")])
        for tournament in tournaments:
            print(
                f"{tournament.name} at {tournament.location} on {tournament.date.strftime('%d-%m-%Y')}"
            )
    else:
        color_print([("yellow", "No tournaments found.")])


def play_tournament():
    """Lancer un tournoi avec des rondes successives de type suisse."""
    tournaments = tournament_controller.tournaments
    if not tournaments:
        color_print([("yellow", "No tournaments available.")])
        return

    # Choisir le tournoi à jouer
    choices = [{"name": t.name, "value": t} for t in tournaments]
    selected = prompt(
        {
            "type": "list",
            "name": "tournament",
            "message": "Select a tournament to play:",
            "choices": choices,
        }
    )["tournament"]

    current_round_number = len(selected.rounds) + 1
    sorted_players = sorted(selected.players, key=lambda p: p.score, reverse=True)
    matches = []

    # Créer des paires de joueurs ou gérer les "byes"
    if len(sorted_players) % 2 != 0:
        sorted_players.append(None)

    for i in range(0, len(sorted_players), 2):
        if sorted_players[i + 1] is None:
            color_print([("yellow", f"{sorted_players[i].first_name} has a bye.")])
        else:
            matches.append(Match(sorted_players[i], sorted_players[i + 1]))

    # Créer et jouer un nouveau tour
    new_round = Round(current_round_number, matches)
    new_round.play_round()
    selected.rounds.append(new_round)
    tournament_controller.save_tournament(selected)

    color_print([("green", f"Round {current_round_number} completed!")])

    # Demander si un autre tour doit être joué
    continue_prompt = prompt(
        {
            "type": "confirm",
            "name": "continue",
            "message": "Play another round?",
            "default": True,
        }
    )["continue"]

    if continue_prompt:
        play_tournament()
    else:
        tournament_controller.generate_report(selected)
        color_print([("green", "Tournament report generated.")])
