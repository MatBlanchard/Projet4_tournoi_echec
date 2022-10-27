from models.singleton import Singleton
from views.create_tournament_view import CreateTournament
from views.load_tournament_view import LoadTournament
from views.report_view import ReportView
from views.view import View
from views.player_view import CreatePlayer


class MainMenu(View, metaclass=Singleton):

    def show(self):
        from controllers.controller import Controller
        print("Bienvenue dans ce programme de gestion de tournoi d'échec:")
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
                    LoadTournament().show(self.tournament_input("Quel tournoi voulez-vous charger?\n"))
            elif user_input == "2":
                CreatePlayer().show()
            elif user_input == "3":
                player_input = self.player_input()
                self.update_rank(player_input)
            elif user_input == "4":
                ReportView().show()
            elif user_input == "q" or user_input == "Q":
                print("Fin du programme")
                break

    @staticmethod
    def main_input():
        while True:
            value = input("Que voulez-vous faire ?\n"
                          "0 - Créer un tournoi\n"
                          "1 - Charger un tournoi\n"
                          "2 - Créer un joueur\n"
                          "3 - Modifier le classement d'un joueur\n"
                          "4 - Voir les rapports\n"
                          "q - Quitter\n>")
            if value in ["0", "1", "2", "3", "4", "q", "Q"]:
                return value
            else:
                print("Veuillez entrer une valeur valide")

    def player_input(self):
        from controllers.controller import Controller
        while True:
            display = "De quel joueur voulez-vous modifier le classement?\n"
            assertions = []
            for p in self.id_sort(Controller().players):
                display += str(p) + "\n"
                assertions.append(str(p.id))
            value = input(display + ">")
            if value in assertions:
                return Controller().get_player_by_id(int(value))
            else:
                print("Veuillez entrer une valeur valide")
                continue
