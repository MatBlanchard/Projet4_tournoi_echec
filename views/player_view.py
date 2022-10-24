from models.player import Player
from models.singleton import Singleton
from views.view import View


class CreatePlayer(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        name = input("Nom du joueur:\n>")
        first_name = input("Prénom du joueur:\n>")
        dob = self.dob_input()
        sex = self.sex_input()
        rank = self.rank_input()
        Controller().create_player(name, first_name, dob, sex, rank)


    # Inputs
    def dob_input(self):
        while True:
            value = input("Date de naissance (format DD-MM-YYYY):\n>")
            try:
                return self.get_date(value)
            except ValueError:
                print("Veuillez entrer une date au format valide: DD-MM-YYYY")

    @staticmethod
    def sex_input():
        while True:
            value = input("Sexe (H ou F):\n>")
            if value in ["H", "h", "F", "f"]:
                return value.upper()
            else:
                print("Veuillez entrer H ou F")

    @staticmethod
    def rank_input():
        while True:
            value = input("Classement:\n>")
            if value.isnumeric():
                if int(value) > 0:
                    return int(value)
                else:
                    print("Veuillez entrer une valeur supérieure à 0")
            else:
                print("Veuillez entrer une valeur numérique valide.")
    ##################################################################

class LoadPlayer(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        print("Voici la liste des joueurs:")
        for p in Controller().players:
            print("nom: " + p.name + " | prénom: " + p.first_name + " | date_naissance: " + p.date_of_birth.strftime("%d/%m/%Y")
                  + " | sexe: " + p.sex + " | classement: " + str(p.rank))
        self.leave_input()

    @staticmethod
    def leave_input():
        while True:
            value = input("r - retour:\n>")
            if value == "r":
                return value
            else:
                print("Veuillez entrer r pour quitter")
