from models.singleton import Singleton
from views.player_view import LoadPlayer
from views.view import View


class ReportView(View, metaclass=Singleton):

    def show(self):
        from controllers.controller import Controller
        while True:
            report_input = self.report_input()
            if report_input == "0":
                LoadPlayer().show(Controller().players)
            elif report_input == "1":
                tournament_input = self.tournament_input("De quel tournoi voulez-vous voir les joueurs?\n")
                if tournament_input != "quit":
                    LoadPlayer().show(tournament_input.players)
            elif report_input == "2":
                print("Voici la liste des tournois")
                if len(Controller().tournaments) == 0:
                    print("Il n'y a aucun tournoi dans la base de données")
                else:
                    for t in Controller().tournaments:
                        if t.status == "in progress":
                            fin = "en cours"
                        else:
                            fin = t.ending_date.strftime("%d/%m/%Y")
                        print("nom: " + t.name + " | lieu: " + t.place + " | début: " +
                              t.starting_date.strftime("%d/%m/%Y") + " | fin: " + fin + " | cadence: " + t.time_control
                              + " | nb joueurs: " + str(len(t.players)) +
                              " | nb tours: " + str(t.nb_rounds) + " | description: " + t.description)
                self.leave_input()
            elif report_input == "3":
                tournament_input = self.tournament_input("De quel tournoi voulez-vous voir les rondes?\n")
                if tournament_input != "quit":
                    if len(tournament_input.rounds) == 0:
                        print("Il n'y a aucune ronde débutée dans ce tournoi")
                    else:
                        while True:
                            round_input = self.rounds_input(tournament_input.rounds)
                            if round_input != "quit":
                                self.display_round_result(round_input)
                                self.leave_input()
                            else:
                                break
            elif report_input == "4":
                tournament_input = self.tournament_input("De quel tournoi voulez-vous voir les matchs?\n")
                if tournament_input != "quit":
                    nb_matchs = 0
                    for r in tournament_input.rounds:
                        nb_matchs += len(r.matchs)
                    if nb_matchs == 0:
                        print("Il n'y a aucun match joué dans ce tournoi")
                    else:
                        for r in tournament_input.rounds:
                            print(r.name.capitalize() + ":")
                            for m in r.matchs:
                                print(" " + m)
                        self.leave_input()
            elif report_input in ["r", "R"]:
                break

    @staticmethod
    def report_input():
        while True:
            value = input("Quel rapport voulez-vous voir ?\n"
                          "0 - Liste de tout joueurs\n"
                          "1 - Liste des joueurs d'un tournoi\n"
                          "2 - Liste de tout les tournois \n"
                          "3 - Liste de toute les rondes d'un tournoi \n"
                          "4 - Liste de tout les matchs d'un tournoi \n"
                          "r - Retour\n>")
            if value in ["0", "1", "2", "3", "4", "r", "R"]:
                return value
            else:
                print("Veuillez entrer une valeur valide")

    @staticmethod
    def rounds_input(rounds):
        from controllers.controller import Controller
        while True:
            display = "De quelle ronde voulez-vous voir les détails?\n"
            assertions = []
            for r in rounds:
                display += str(r) + "\n"
                assertions.append(str(r.id))
            assertions.append("r")
            assertions.append("R")
            value = input(display + "r - Retour\n>")
            if value in ["r", "R"]:
                return "quit"
            if value in assertions:
                return Controller().get_round_by_id(int(value))
            else:
                print("Veuillez entrer une valeur valide")
                continue
