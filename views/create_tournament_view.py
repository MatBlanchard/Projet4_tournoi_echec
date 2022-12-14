from views.view import View
from models.singleton import Singleton


class CreateTournament(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        name = input("Nom du tournoi:\n>")
        place = input("Lieu du tournoi:\n>")
        starting_date = self.date_input()
        time_control = self.time_control_input()
        nb_players = self.nb_players_input()
        players = self.players_input(nb_players)
        nb_rounds = self.nb_rounds_input(nb_players)
        description = input("Description:\n>")
        Controller().create_tournament(name, place, starting_date, time_control, players, nb_rounds, description)
        if not self.play_input():
            return False
        else:
            return True

    # Inputs
    def date_input(self):
        while True:
            value = input("Date de début du tournoi (format DD-MM-YYYY):\n>")
            try:
                return self.get_date(value)
            except ValueError:
                print("Veuillez entrer une date au format valide: DD-MM-YYYY")

    @staticmethod
    def time_control_input():
        while True:
            value = input("Cadence du tournoi:\n"
                          "0 - Bullet\n"
                          "1 - Blitz\n"
                          "2 - Rapid\n>")
            if value in ["0", "1", "2"]:
                if value == "0":
                    return "Bullet"
                elif value == "1":
                    return "Blitz"
                elif value == "2":
                    return "Rapid"
            else:
                print("Veuillez entrer une valeur valide")

    @staticmethod
    def nb_players_input():
        from controllers.controller import Controller
        while True:
            value = input("Combien de joueurs voulez-vous ajouter ?\n>")
            if not value.isnumeric():
                print("Veuillez rentrer une valeur numérique valide")
                continue
            if int(value) <= 0:
                print("Veuillez rentrer une valeur supérieure à 0")
                continue
            if int(value) > len(Controller().players):
                print("Il n'y a que " + str(len(Controller().players)) + " dans la base de données")
                continue
            if int(value) % 2 != 0:
                print("Veuillez rentrer un nombre pair")
                continue
            return int(value)

    @staticmethod
    def players_input(nb_players):
        from controllers.controller import Controller
        while True:
            players = []
            while len(players) < nb_players:
                display = "Quel joueur voulez-vous ajouter?\n"
                assertions = []
                for p in Controller().players:
                    if p not in players:
                        display += str(p) + "\n"
                        assertions.append(str(p.id))
                value = input(display + ">")
                if value in assertions:
                    players.append(Controller().get_player_by_id(int(value)))
                else:
                    print("Veuillez entrer une valeur valide")
                    continue
            return players

    @staticmethod
    def nb_rounds_input(nb_players):
        while True:
            if nb_players == 2:
                return 1
            else:
                value = input("Nombre de tour (4 par défaut):\n>")
                if nb_players > 4 and value == "":
                    return 4
                if value.isnumeric():
                    if int(value) > 0:
                        return int(value)
                    else:
                        print("Veuillez entrer une valeur supérieure à 0")
                else:
                    print("Veuillez entrer une valeur numérique valide.")

    @staticmethod
    def play_input():
        while True:
            value = input("Jouer le tournoi? (Y/N)\n>")
            if value in ["y", "Y", "n", "N"]:
                if value in ["y", "Y"]:
                    return True
                else:
                    return False
            else:
                print("Veuillez entrer une valeur valide")
    ###################################################################################################################
