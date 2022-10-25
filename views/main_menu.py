from models.singleton import Singleton
from views.create_tournament_view import CreateTournament
from views.load_tournament_view import LoadTournament
from views.view import View
from views.player_view import CreatePlayer, LoadPlayer


class MainMenu(View, metaclass=Singleton):

    def show(self):
        from controllers.controller import Controller
        while True:
            user_input = self.main_input()
            if user_input == "0":
                if len(Controller().players) < 2:
                    print("Il faut d'abord créer au moins 2 joueurs")
                else:
                    if CreateTournament().show():
                        LoadTournament().show(Controller().tournaments[len(Controller().tournaments)-1])
            elif user_input == "1":
                if len(Controller().tournaments) == 0:
                    print("Il n'y a aucun tournoi dans la base de données")
                else:
                    LoadTournament().show(self.tournament_input())
            elif user_input == "2":
                CreatePlayer().show()
            elif user_input == "3":
                report_input = self.report_input()
                if report_input == "0":
                    LoadPlayer().show()
            elif user_input == "q" or user_input == "Q":
                break

    @staticmethod
    def main_input():
        while True:
            value = input("Que voulez-vous faire ?\n"
                          "0 - Créer un tournoi\n"
                          "1 - Charger un tournoi\n"
                          "2 - Créer un joueur\n"
                          "3 - Voir les rapports\n"
                          "q - Quitter\n> ")
            if value in ["0", "1", "2", "3", "4", "q", "Q"]:
                return value
            else:
                print("Veuillez entrer une valeur valide")

    @staticmethod
    def tournament_input():
        from controllers.controller import Controller
        while True:
            display = "Quel tournoi voulez-vous charger?\n"
            assertions = []
            for t in Controller().tournaments:
                display += str(t) + "\n"
                assertions.append(str(t.id))
            value = input(display + ">")
            if value in assertions:
                return Controller().get_tournament_by_id(int(value))
            else:
                print("Veuillez entrer une valeur valide")
                continue

    @staticmethod
    def report_input():
        while True:
            value = input("Quel rapport voulez-vous voir ?\n"
                          "0 - Liste des joueurs\n"
                          "r - Retour\n> ")
            if value in ["0", "1", "2", "3", "4", "q", "Q"]:
                return value
            else:
                print("Veuillez entrer une valeur valide")
