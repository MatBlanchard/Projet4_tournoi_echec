from datetime import *
from models.enumeration import Sexe

class Joueur:
    def __init__(self, nom:str, prenom:str, date_naissance:date, sexe:Sexe, classement:int):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement

    #Getters
    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @property
    def date_naissance(self) -> date:
        return self.__date_naissance

    @property
    def sexe(self) -> Sexe:
        return self.__sexe

    @property
    def classement(self) -> int:
        return self.__classement

    #Setters
    @nom.setter
    def nom(self, nom:str):
        if type(nom) == str:
            self.__nom = nom
        else:
            raise TypeError("argument in Joueur.nom() is not the expected type. Expected type : str")

    @prenom.setter
    def prenom(self, prenom:str):
        if type(prenom) == str:
            self.__prenom = prenom
        else:
            raise TypeError("argument in Joueur.prenom() is not the expected type. Expected type : str")

    @date_naissance.setter
    def date_naissance(self, date_naissance:date):
        if type(date_naissance) == date:
            self.__date_naissance = date_naissance
        else:
            raise TypeError("argument in Joueur.date_naissance() is not the expected type. Expected type : date")

    @sexe.setter
    def sexe(self, sexe:Sexe):
        if  type(sexe) == Sexe:
            self.__sexe = sexe
        else:
            raise TypeError("argument in Joueur.sexe() is not the expected type. Expected type : Sexe")

    @classement.setter
    def classement(self, classement:int):
        if type(classement) == int:
            if classement >= 0:
                self.__classement = classement
            else :
                raise ValueError("argument in Joueur.classement() is negative. Argument must be a positive integer")
        else:
            raise TypeError("argument in Joueur.classement() is not the expected type. Expected type : int")

    def __str__(self):
        return self.nom.upper() + " " + self.prenom + " " + self.date_naissance.strftime("%d/%m/%Y")

