class Match:
    def __init__(self, joueurs):
        self.joueurs = joueurs

    #Getters
    @property
    def joueurs(self) -> list:
        return self.__joueurs

    @property
    def scores(self) -> list:
        return self.__scores

    #Setters
    @joueurs.setter
    def joueurs(self, joueurs:list):
        if type(joueurs) == list:
            self.__joueurs = joueurs
        else:
            raise TypeError("argument in Match.joueurs() is not the expected type. Expected type : list")

    @scores.setter
    def scores(self, scores:list):
        if type(scores) == list:
            self.__scores = scores
        else:
            raise TypeError("argument in Match.scores() is not the expected type. Expected type : list")

    def __str__(self):
        return "[joueurs: " + self.joueurs + " | scores: " + str(self.scores) + "]"