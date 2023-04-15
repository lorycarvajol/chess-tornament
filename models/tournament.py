class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.description = description
        self.rounds = []
        self.players = []
        self.current_round = 0
