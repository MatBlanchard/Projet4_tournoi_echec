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
        while True:
            players = []
            user_input = self.sort_input()
            if user_input == "0":
                players = self.alphabetical_sort(Controller().players)
                sort = "par ordre alphabétique"
            elif user_input == "1":
                players = self.rank_sort(Controller().players)
                sort = "par classement"
            elif user_input == "r":
                break
            print("Voici la liste des joueurs " + sort + ":")
            for p in players:
                print("nom: " + p.name + " | prénom: " + p.first_name + " | date_naissance: " +
                      p.dob.strftime("%d/%m/%Y") + " | sexe: " + p.sex + " | classement: " + str(p.rank))
            self.leave_input()

    @staticmethod
    def sort_input():
        while True:
            value = input("Comment voulez-vous trier les joueurs ?\n"
                          "0 - Par odre alphabétique\n"
                          "1 - Par classement\n"
                          "r - Retour\n>")
            if value in ["0", "1", "r"]:
                return value
            else:
                print("Veuillez entrer une valeur valide")

    @staticmethod
    def leave_input():
        while True:
            value = input("r - retour:\n>")
            if value == "r":
                return value
            else:
                print("Veuillez entrer r pour revenir en arriere")
