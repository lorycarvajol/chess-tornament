from InquirerPy import prompt
from InquirerPy.utils import color_print
from controllers.player_controller import PlayerController

player_controller = PlayerController()


def add_player_form():
    questions = [
        {
            "type": "input",
            "name": "first_name",
            "message": "Enter first name:",
            "validate": lambda text: True if text else "First name is required",
        },
        {
            "type": "input",
            "name": "last_name",
            "message": "Enter last name:",
            "validate": lambda text: True if text else "Last name is required",
        },
        {
            "type": "input",
            "name": "date_of_birth",
            "message": "Enter date of birth (DD-MM-YYYY):",
            "validate": lambda text: True if text else "Date of birth is required",
        },
        {
            "type": "input",
            "name": "national_id",
            "message": "Enter national ID:",
            "validate": lambda text: True if text else "National ID is required",
        },
    ]

    answers = prompt(questions)
    player_controller.add_player(**answers)
    color_print([("green", "Player added successfully!")])


def list_players():
    players = player_controller.get_all_players()
    if players:
        color_print([("cyan", "\nList of Players:")])
        for player in players:
            print(
                f"{player.first_name} {player.last_name}, ID: {player.national_id}, Date of Birth: {player.date_of_birth.strftime('%d-%m-%Y')}"
            )
    else:
        color_print([("yellow", "\nNo players found.")])
