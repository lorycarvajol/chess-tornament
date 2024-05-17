from InquirerPy import prompt
from colorama import Fore, Style


def get_tournament_details():
    questions = [
        {"type": "input", "name": "name", "message": "Enter tournament name:"},
        {"type": "input", "name": "location", "message": "Enter location:"},
        {"type": "input", "name": "date", "message": "Enter date (DD-MM-YYYY):"},
    ]
    return prompt(questions)
