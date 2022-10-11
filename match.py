class Match:
    def __init__(self, joueurs):
        self.setJoueurs(joueurs)
        self.setScores(0)

    #Setters
    def setJoueurs(self, joueurs):
        self.joueurs = joueurs

    def setScores(self, scores):
        self.scores = scores

    #Getters
    def getJoueurs(self):
        return self.joueurs

    def getScores(self):
        return self.scores

    def __str__(self):
        return "[joueurs: " + self.getJoueurs() + " | scores: " + str(self.getScores()) + "]"