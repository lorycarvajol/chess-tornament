from controllers.tournament_controller import create_tournament

def get_tournament_info():
    name = input("Enter the tournament name: ")
    location = input("Enter the tournament location: ")
    start_date = input("Enter the tournament start date (YYYY-MM-DD): ")
    end_date = input("Enter the tournament end date (YYYY-MM-DD): ")
    num_rounds = int(input("Enter the number of rounds (default: 4): ") or "4")
    description = input("Enter a description (optional): ")
    return name, location, start_date, end_date, num_rounds, description

def add_tournament():
    name, location, start_date, end_date, num_rounds, description = get_tournament_info()
    create_tournament(name, location, start_date, end_date, num_rounds, description)
    print(f"Tournament {name} added successfully!")
