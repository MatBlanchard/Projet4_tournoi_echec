from Models.enumeration import Cadence

class Tournoi:
    def __init__(self, nom, lieu, date):
        self.setNom(nom)
        self.setLieu(lieu)
        self.setDate(date)

    #Setters
    def setNom(self, nom):
        if type(nom) == str:
            self.__nom = nom
        else:
            raise TypeError("argument in Tournoi.setNom() is not the expected type. Expected type : str")

    def setLieu(self, lieu):
        if type(lieu) == str:
            self.__lieu = lieu
        else:
            raise TypeError("argument in Tournoi.setLieu() is not the expected type. Expected type : str")

    def setDate(self, date):
        if type(date) == date:
            self.__date = date
        else:
            raise TypeError("argument in Tournoi.setDate() is not the expected type. Expected type : date")

    def setTour(self, tour=4):
        if type(tour) == int:
            if tour > 0:
                self.__tour = tour
            else:
                raise ValueError("argument in Tournoi.setTourt() is negative or nul. Argument must be a strictly positive integer")
        else:
            raise TypeError("argument in Tournoi.setTour() is not the expected type. Expected type : int")

    def setTournees(self, tournees):
        if type(tournees) == list:
            self.__tournees = tournees
        else:
            raise TypeError("argument in Tournoi.setTournees() is not the expected type. Expected type : list")

    def setJoueurs(self, joueurs):
        if type(joueurs) == list:
            self.__joueurs = joueurs
        else:
            raise TypeError("argument in Tournoi.setJoueurs() is not the expected type. Expected type : list")

    def setCadence(self, cadence):
        if type(cadence) == Cadence:
            self.__cadence = cadence
        else:
            raise TypeError("argument in Tournoi.setCadence() is not the expected type. Expected type : Cadence")

    def setDescription(self, description):
        if type(description) == str:
            self.__description = description
        else:
            raise TypeError("argument in Tournoi.setDescription() is not the expected type. Expected type : str")

    #Getters
    def getNom(self):
        return self.__nom

    def getLieu(self):
        return self.__lieu

    def getDate(self):
        return self.__date

    def getTour(self):
        return self.__tour

    def getTournees(self):
        return self.__tournees

    def getJoueurs(self):
        return self.__joueurs

    def getCadence(self):
        return self.__cadence

    def getDescription(self):
        return self.__description

    def __str__(self):
        return "[nom: " + self.getNom() + " | lieu: " + self.getLieu() + " | date: " + str(self.getDate()) + " | tour: " + str(self.getTour()) + "]"

def main():
    pass


if __name__=="__main__":
    main()