```markdown
♟️ Gestionnaire de Tournois d'Échecs ♟️
Bienvenue dans Chess Tournament – votre outil ultime pour organiser et gérer des tournois d'échecs. 
Cette application vous aide à gérer les joueurs, organiser des tournois, 
mener des rondes en système suisse et générer des rapports complets. Commençons !

🚀 Fonctionnalités
Gestion des joueurs : Ajouter, lister et gérer facilement les joueurs.
Gestion des tournois : Créer des tournois, ajouter des joueurs et gérer les rondes.
Rondes en système suisse : Générer automatiquement des rondes et déterminer les vainqueurs des matchs.
Rapports complets : Générer des rapports PDF détaillés des résultats des tournois.
📋 Prérequis
Avant de commencer, assurez-vous de répondre aux exigences suivantes :

Python 3.12+
Bibliothèque fpdf pour la génération de PDF
Bibliothèque InquirerPy pour les invites interactives
Vous pouvez installer les bibliothèques nécessaires avec la commande suivante :

bash
Copier le code
pip install InquirerPy fpdf
```

## 🛠️ Installation

Clonez le dépôt sur votre machine locale :

```bash
git clone https://github.com/lorycarvajol/chess-tornament.git
cd chess-tournament
```

## 📖 Utilisation

### Menu Principal

1. **Gestionnaire de Tournois**

   - **Ajouter un Tournoi** : Créer un nouveau tournoi en entrant son nom, son lieu et sa date.
   - **Lancer un Tournoi** : Sélectionner un tournoi, ajouter des joueurs et démarrer les rondes en système suisse.
   - **Retourner au Menu Principal** : Retourner au menu principal.
2. **Gestionnaire de Joueurs**

   - **Ajouter un Joueur** : Ajouter un nouveau joueur à la base de données.
   - **Lister les Joueurs** : Voir tous les joueurs enregistrés.
   - **Retourner au Menu Principal** : Retourner au menu principal.

### Exemple de Commandes

Lancez l'application :

```bash
python main.py
```

Suivez les invites pour naviguer dans les menus et gérer vos tournois. Par exemple, pour ajouter un nouveau tournoi :

1. Sélectionnez **Gestionnaire de Tournois** dans le menu principal.
2. Sélectionnez **Ajouter un Tournoi**.
3. Entrez le nom du tournoi, le lieu et la date au format JJ-MM-AAAA.

### Lancer un Tournoi

1. Sélectionnez **Lancer un Tournoi** dans le menu **Gestionnaire de Tournois**.
2. Choisissez un tournoi dans la liste.
3. Sélectionnez les joueurs pour ce tournoi.
4. Le tournoi commencera et vous serez invité à sélectionner les vainqueurs pour chaque match.

### Génération de Rapports

À la fin du tournoi, un rapport PDF sera généré contenant :

- Les scores finaux
- Les résultats des matchs par ronde
- Le vainqueur du tournoi

Le PDF sera sauvegardé dans le répertoire `data`.

## 🤝 Contribuer

Les contributions sont les bienvenues ! Veuillez forker le dépôt et créer une pull request. Pour les changements majeurs, veuillez ouvrir d'abord une issue pour discuter de ce que vous souhaitez changer.

## 🧑‍💻 Auteurs

- **Lory Carvajol** - *Travail initial* - https://github.com/lorycarvajol/chest-tornament

Voir aussi la liste des [contributeurs](https://github.com/votre-nom-utilisateur/tournament-manager/contributors) ayant participé à ce projet.

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

Profitez de la gestion de vos tournois avec **Chess Tournament** ! Faisons en sorte que chaque coup compte ! ♟️

---

# ♟️ Chess Tournament ♟️

Welcome to **Tournament Manager** – your ultimate tool for organizing and managing chess tournaments. This application helps you manage players, set up tournaments, run Swiss-system rounds, and generate comprehensive reports. Let's get started!

## 🚀 Features

- **Player Management**: Add, list, and manage players with ease.
- **Tournament Management**: Create tournaments, add players, and manage rounds.
- **Swiss-System Rounds**: Automatically generate rounds and determine match winners.
- **Comprehensive Reporting**: Generate detailed PDF reports of tournament results.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12+
- `fpdf` library for PDF generation
- `InquirerPy` library for interactive prompts

You can install the necessary libraries using the following command:

```bash
pip install InquirerPy fpdf 
```

## 🛠️ Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/lorycarvajol/chess-tornament.git
cd chess-tournament
```

## 📖 Usage

### Main Menu

1. **Tournament Manager**

   - **Add Tournament**: Create a new tournament by entering its name, location, and date.
   - **Play Tournament**: Select a tournament, add players, and start Swiss-system rounds.
   - **Return to Main Menu**: Go back to the main menu.
2. **Player Manager**

   - **Add Player**: Add a new player to the database.
   - **List Players**: View all registered players.
   - **Return to Main Menu**: Go back to the main menu.

### Example Commands

Run the application:

```bash
python main.py
```

Follow the prompts to navigate through the menus and manage your tournaments. For example, to add a new tournament:

1. Select **Tournament Manager** from the main menu.
2. Select **Add Tournament**.
3. Enter the tournament name, location, and date in DD-MM-YYYY format.

### Running a Tournament

1. Select **Play Tournament** from the **Tournament Manager** menu.
2. Choose a tournament from the list.
3. Select the players for this tournament.
4. The tournament will start, and you'll be prompted to select the winners for each match.

### Generating Reports

At the end of the tournament, a PDF report will be generated containing:

- Final scores
- Match results by round
- The tournament winner

The PDF will be saved in the `data` directory.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

## 🧑‍💻 Authors

- **Lory Carvajol** - *Initial work* - https://github.com/lorycarvajol/chest-tornament

See also the list of [contributors](https://github.com/your-username/tournament-manager/contributors) who participated in this project.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Enjoy managing your tournaments with Chess Tournament! Let's make every move count! ♟️

```

```

```

```
