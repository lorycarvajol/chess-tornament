class Player:
    def __init__(self, first_name, last_name, birthdate, player_id=None):
        """
        Initialise un joueur avec son prénom, nom de famille, date de naissance et un ID optionnel.

        Args:
            first_name (str): Prénom du joueur.
            last_name (str): Nom de famille du joueur.
            birthdate (str): Date de naissance du joueur au format DD-MM-YYYY.
            player_id (int, optional): ID unique du joueur. Si None, l'ID sera généré plus tard.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.id = player_id
        print(
            f"Player initialisé : {self.first_name} {self.last_name}, Date de naissance : {self.birthdate}, ID : {self.id}"
        )

    def to_dict(self):
        """
        Convertit l'objet Player en dictionnaire.

        Returns:
            dict: Représentation dictionnaire de l'objet Player.
        """
        player_dict = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
        }
        #    print(f"Player converti en dictionnaire : {player_dict}")
        return player_dict

    @classmethod
    def from_dict(cls, data):
        """
        Crée un objet Player à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du joueur.

        Returns:
            Player: Objet Player initialisé avec les données fournies.
        """
        player = cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birthdate=data["birthdate"],
            player_id=data.get("id"),
        )
        #       print(f"Player créé à partir du dictionnaire : {data}")
        return player
