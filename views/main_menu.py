from models.singleton import Singleton
from views.create_tournament_view import CreateTournament
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
                        LoadTournament().show(Controller.tournaments[len(Controller.tournaments)-1])
            elif user_input == "2":
                CreatePlayer().show()
            elif user_input == "3":
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
