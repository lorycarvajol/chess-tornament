class MatchController:
    def __init__(self):
        self.matches = []

    def add_match(self, joueur1, joueur2, score_joueur1=None, score_joueur2=None):
        match = match(joueur1, joueur2, score_joueur1, score_joueur2)
        self.matches.append(match)
        return match

    def find_match(self, joueur1, joueur2):
        for match in self.matches:
            if (match.joueur1 == joueur1 and match.joueur2 == joueur2) or (
                match.joueur1 == joueur2 and match.joueur2 == joueur1
            ):
                return match
        return None

    def list_matches(self):
        return self.matches
