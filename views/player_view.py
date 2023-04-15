from controllers.player_controller import create_player

def get_player_info():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    date_of_birth = input("Enter the date of birth (YYYY-MM-DD): ")
    return first_name, last_name, date_of_birth

def add_player():
    first_name, last_name, date_of_birth = get_player_info()
    create_player(first_name, last_name, date_of_birth)
    print(f"Player {first_name} {last_name} added successfully!")
