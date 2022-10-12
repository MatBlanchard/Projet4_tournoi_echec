class Ronde:
    def __init__(self):
        pass

    #Setters
    def setMatchs(self, matchs):
        if type(matchs) == list:
            self.__matchs = matchs
        else:
            raise TypeError("argument in Ronde.setMatchs() is not the expected type. Expected type : list")

    #Getters
    def getMatchs(self):
        return self.__matchs

    def __str__(self):
        return ""