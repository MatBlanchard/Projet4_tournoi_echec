from datetime import *
from colorama import Fore
from error import *
from sexe import Sexe


class Joueur:
    def __init__(self, nom, prenom, dateNaissance, sexe, classement):
        self.setNom(nom)
        self.setPrenom(prenom)
        self.setDateNaissance(dateNaissance)
        self.setSexe(sexe)
        self.setClassement(classement)

    #Setters
    def setNom(self, nom):
        if type(nom) == str:
            self.__nom = nom
        else:
            raise NomError("argument in Joueur.setNom() is not the expected type. Expected type : str")

    def setPrenom(self, prenom):
        if type(prenom) == str:
            self.__prenom = prenom
        else:
            raise PrenomError("argument in Joueur.setPrenom() is not the expected type. Expected type : str")

    def setDateNaissance(self, dateNaissance):
        if type(dateNaissance) == date:
            self.__dateNaissance = dateNaissance
        else:
            raise DateNaissanceError("argument in Joueur.setDateNaissance() is not the expected type. Expected type : date")

    def setSexe(self, sexe):
        if  type(sexe) == Sexe:
            self.__sexe = sexe
        else:
            raise SexeError("argument in Joueur.setSexe() is not the expected type. Expected type : sexe")

    def setClassement(self, classement):
        if type(classement) == int:
            if classement >= 0:
                self.__classement = classement
            else :
                raise ClassementError("argument in Joueur.setClassement() is negative. Argument must be a positive int")
        else:
            raise ClassementError("argument in Joueur.setClassement() is not the expected type. Expected type : int")

    #Getters
    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getDateNaissance(self):
        return self.__dateNaissance

    def getSexe(self):
        return self.__sexe

    def getClassement(self):
        return self.__classement

    def __str__(self):
        return "[nom: " + self.getNom() + " | prenom: " + self.getPrenom() + " | dateNaissance: " + \
               str(self.getDateNaissance()) + " | sexe: " + str(self.getSexe()) + " | classement: " + str(self.getClassement()) + "]"

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
    except NomError:
        print("TEST 2 | mauvais type de \"nom\" | validé")

    #Test 3 : mauvais type de "prenom"
    try:
        joueur = Joueur("a", 1, date.today(), Sexe.HOMME, 2500)
        print(Fore.RED + "TEST 3 | le \"prenom\" doit étre une chaine de caractéres | non validé" + Fore.RESET)
    except PrenomError:
        print("TEST 3 | mauvais type de \"prenom\" | validé")

    #Test 4 : mauvais type de "dateNaissance"
    try:
        joueur = Joueur("a", "a", 1, Sexe.HOMME, 2500)
        print(Fore.RED + "TEST 4 | la \"dateNaissance\" doit étre une date | non validé" + Fore.RESET)
    except DateNaissanceError:
        print("TEST 4 | mauvais type de \"dateNaissance\" | validé")

    #Test 5 : mauvais type de "sexe"
    try:
        joueur = Joueur("a", "a", date.today(), "h", 2500)
        print(Fore.RED + "TEST 5 | le \"sexe\" doit étre un sexe | non validé" + Fore.RESET)
    except SexeError:
        print("TEST 5 | mauvais type de \"sexe\" | validé")

    #Test 6 : mauvais type de "classement"
    try:
        joueur = Joueur("a", "a", date.today(), Sexe.HOMME, "2500")
        print(Fore.RED + "TEST 6 | le \"classement\" doit étre un int | non validé" + Fore.RESET)
    except ClassementError:
        print("TEST 6 | mauvais type de \"classement\" | validé")

    #Test 7 : classement < 0
    try:
        joueur = Joueur("a", "a", date.today(), Sexe.HOMME, -2500)
        print(Fore.RED + "TEST 7 | le \"classement\" doit étre supérieur à 0 | non validé" + Fore.RESET)
    except ClassementError:
        print("TEST 7 | classement < 0 | validé")

    print("TEST 8 | str | " + str(Joueur("a", "a", date.today(), Sexe.HOMME, 2500)))


if __name__=="__main__":
    main()