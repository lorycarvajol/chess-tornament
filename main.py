from views.player_view import add_player
from views.tournament_view import add_tournament
from views.round_view import create_new_round, add_match_to_round, update_match_result, mark_round_as_completed

def main():
    players = []
    tournaments = []

    while True:
        print("\n1. Add player")
        print("2. Add tournament")
        print("3. Create round")
        print("4. Add match")
        print("5. Update match score")
        print("6. End round")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_player()
        elif choice == "2":
            add_tournament()
        elif choice == "3":
            tournament_id = int(input("Enter tournament ID: "))
            create_new_round(tournaments[tournament_id])
        elif choice == "4":
            tournament_id = int(input("Enter tournament ID: "))
            add_match_to_round(tournaments[tournament_id], players)
        elif choice == "5":
            tournament_id = int(input("Enter tournament ID: "))
            update_match_result(tournaments[tournament_id])
        elif choice == "6":
            tournament_id = int(input("Enter tournament ID: "))
            mark_round_as_completed(tournaments[tournament_id])
        elif choice == "7":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
