from views.main_menu import main_menu

if __name__ == "__main__":
    print("Bienvenue dans le gestionnaire de tournois de jeux d'échecs !")
    print("Utilisez les options du menu pour naviguer dans l'application.")
    print("Instructions:")
    print("1. Pour gérer les joueurs, choisissez 'Player Manager'.")
    print("2. Pour gérer les tournois, choisissez 'Tournament Manager'.")
    print("3. Suivez les Instructions pour ajouter, lister ou jouer des tournois.")
    print(
        "4. Pour ajouter un joueur, entrez uniquement des lettres pour le prénom et le nom."
    )
    print("5. Les dates doivent être au format DD-MM-YYYY.")
    print("Profitez de l'application!")
    main_menu()
