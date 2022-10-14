from datetime import *
from colorama import Fore
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
        return "[nom: " + self.nom + " | prenom: " + self.prenom + " | dateNaissance: " + \
               self.date_naissance.strftime("%d/%m/%Y") + " | sexe: " + self.sexe.name + " | classement: " + str(self.classement) + "]"

def main():
    #Test 1 : constructeur vide
    try:
        joueur = Joueur()
        print(Fore.RED + "TEST 1 | le constructeur doit prendre 5 paramètres | non validé" + Fore.RESET)
    except TypeError:
        print("TEST 1 | constructeur vide | validé")

    #Test 2 : mauvais type de "nom"
    try:
        joueur = Joueur(1, "a", date.today(), Sexe.HOMME, 2500)
        print(Fore.RED + "TEST 2 | le \"nom\" doit étre une chaine de caractéres | non validé" + Fore.RESET)
    except TypeError:
        print("TEST 2 | mauvais type de \"nom\" | validé")

    #Test 3 : mauvais type de "prenom"
    try:
        joueur = Joueur("a", 1, date.today(), Sexe.HOMME, 2500)
        print(Fore.RED + "TEST 3 | le \"prenom\" doit étre une chaine de caractéres | non validé" + Fore.RESET)
    except TypeError:
        print("TEST 3 | mauvais type de \"prenom\" | validé")

    #Test 4 : mauvais type de "dateNaissance"
    try:
        joueur = Joueur("a", "a", 1, Sexe.HOMME, 2500)
        print(Fore.RED + "TEST 4 | la \"dateNaissance\" doit étre une date | non validé" + Fore.RESET)
    except TypeError:
        print("TEST 4 | mauvais type de \"dateNaissance\" | validé")

    #Test 5 : mauvais type de "sexe"
    try:
        joueur = Joueur("a", "a", date.today(), "h", 2500)
        print(Fore.RED + "TEST 5 | le \"sexe\" doit étre un sexe | non validé" + Fore.RESET)
    except TypeError:
        print("TEST 5 | mauvais type de \"sexe\" | validé")

    #Test 6 : mauvais type de "classement"
    try:
        joueur = Joueur("a", "a", date.today(), Sexe.HOMME, "2500")
        print(Fore.RED + "TEST 6 | le \"classement\" doit étre un int | non validé" + Fore.RESET)
    except TypeError:
        print("TEST 6 | mauvais type de \"classement\" | validé")

    #Test 7 : classement < 0
    try:
        joueur = Joueur("a", "a", date.today(), Sexe.HOMME, -2500)
        print(Fore.RED + "TEST 7 | le \"classement\" doit étre supérieur à 0 | non validé" + Fore.RESET)
    except ValueError:
        print("TEST 7 | classement < 0 | validé")

    print("TEST 8 | str | " + str(Joueur("a", "a", date.today(), Sexe.HOMME, 2500)))


if __name__=="__main__":
    main()