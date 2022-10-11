class Match:
    def __init__(self, joueurs):
        self.setJoueurs(joueurs)

    #Setters
    def setJoueurs(self, joueurs):
        if type(joueurs) == list:
            self.__joueurs = joueurs
        else:
            raise TypeError("argument in Match.setJoueurs() is not the expected type. Expected type : list")

    def setScores(self, scores):
        if type(scores) == list:
            self.__scores = scores
        else:
            raise TypeError("argument in Match.setScrores() is not the expected type. Expected type : list")

    #Getters
    def getJoueurs(self):
        return self.__joueurs

    def getScores(self):
        return self.__scores

    def __str__(self):
        return "[joueurs: " + self.getJoueurs() + " | scores: " + str(self.getScores()) + "]"