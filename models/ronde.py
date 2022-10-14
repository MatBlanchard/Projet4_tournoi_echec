class Ronde:
    def __init__(self):
        pass

    #Getters
    @property
    def matchs(self) -> list:
        return self.__matchs

    #Setters
    @matchs.setter
    def matchs(self, matchs:list):
        if type(matchs) == list:
            self.__matchs = matchs
        else:
            raise TypeError("argument in Ronde.matchs() is not the expected type. Expected type : list")

    def __str__(self):
        return ""