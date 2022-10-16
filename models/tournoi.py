from datetime import date
from models.enumeration import Cadence

class Tournoi:
    def __init__(self, nom, lieu, date_debut, tour, tournees, joueurs, cadence, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.tour = tour
        self.tournees = tournees
        self.cadence = cadence
        self.description = description

    #Getters
    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def lieu(self) -> str:
        return self.__lieu

    @property
    def date_debut(self) -> date:
        return self.__date_debut

    @property
    def date_fin(self) -> date:
        return self.__date_fin

    @property
    def tour(self) -> int:
        return self.__tour

    @property
    def tournees(self) -> list:
        return self.__tournees

    @property
    def joueurs(self) -> list:
        return self.__joueurs

    @property
    def cadence(self) -> Cadence:
        return self.__cadence

    @property
    def description(self) -> str:
        return self.__description

    #Setters
    @nom.setter
    def nom(self, nom):
        if type(nom) == str:
            self.__nom = nom
        else:
            raise TypeError("argument in Tournoi.nom() is not the expected type. Expected type : str")

    @lieu.setter
    def lieu(self, lieu):
        if type(lieu) == str:
            self.__lieu = lieu
        else:
            raise TypeError("argument in Tournoi.lieu() is not the expected type. Expected type : str")

    @date_debut.setter
    def date_debut(self, date_debut):
        if type(date_debut) == date_debut:
            self.__date_debut = date_debut
        else:
            raise TypeError("argument in Tournoi.date_debut() is not the expected type. Expected type : date")

    @date_fin.setter
    def date_fin(self, date_fin):
        if type(date_fin) == date_fin:
            self.__date_fin = date_fin
        else:
            raise TypeError("argument in Tournoi.date_fin() is not the expected type. Expected type : date")

    @tour.setter
    def tour(self, tour):
        if type(tour) == int:
            if tour > 0:
                self.__tour = tour
            else:
                raise ValueError("argument in Tournoi.tour() is negative or nul. Argument must be a strictly positive integer")
        else:
            raise TypeError("argument in Tournoi.tour() is not the expected type. Expected type : int")

    @tournees.setter
    def tournees(self, tournees):
        if type(tournees) == list:
            self.__tournees = tournees
        else:
            raise TypeError("argument in Tournoi.tournees() is not the expected type. Expected type : list")

    @joueurs.setter
    def joueurs(self, joueurs):
        if type(joueurs) == list:
            self.__joueurs = joueurs
        else:
            raise TypeError("argument in Tournoi.joueurs() is not the expected type. Expected type : list")

    @cadence.setter
    def cadence(self, cadence):
        if type(cadence) == Cadence:
            self.__cadence = cadence
        else:
            raise TypeError("argument in Tournoi.cadence() is not the expected type. Expected type : Cadence")

    @description.setter
    def description(self, description):
        if type(description) == str:
            self.__description = description
        else:
            raise TypeError("argument in Tournoi.description() is not the expected type. Expected type : str")

    def __str__(self):
        return "[nom: " + self.nom + " | lieu: " + self.lieu + " | date: " + str(self.date_debut) + " | tour: " + str(self.tour) + "]"

def main():
    pass


if __name__=="__main__":
    main()