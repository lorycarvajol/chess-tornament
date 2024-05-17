from InquirerPy import prompt
from controllers.tournament_controller import add_tournament


class AddTournamentCommand:
    def execute(self):
        # Collecter les données nécessaires pour créer un tournoi
        questions = [
            {"type": "input", "name": "name", "message": "Enter tournament name:"},
            {
                "type": "input",
                "name": "location",
                "message": "Enter tournament location:",
            },
            {
                "type": "input",
                "name": "date",
                "message": "Enter tournament date (DD-MM-YYYY):",
            },
        ]
        answers = prompt(questions)

        # Appeler la fonction pour ajouter un tournoi avec les données collectées
        add_tournament(answers["name"], answers["location"], answers["date"])
