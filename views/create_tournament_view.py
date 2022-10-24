from models.tournament import Tournament
from views.view import View
from models.singleton import Singleton


class CreateTournament(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        # On demande les infos pour créer le tournoi
        name = input("Nom du tournoi:\n>")
        place = input("Lieu du tournoi:\n>")
        starting_date = self.date_input("Date de début du tournoi (format DD/MM/YYYY):\n>")
        time_control = self.time_control_input()
        nb_players = self.nb_players_input()
        players = self.players_input(nb_players)
        nb_matchs = int(nb_players / 2)
        nb_rounds = self.nb_rounds_input(nb_matchs)
        description = input("Description:\n>")
        players_id = []
        for p in players:
            players_id.append(p.id)
        Controller().players.append(Tournament(len(Controller().tournaments) + 1, name, place, starting_date,
                                                   time_control, players, nb_rounds, description))
        tournament = {
                "id": len(Controller().tournaments),
                "name": name,
                "place": place,
                "starting_date": starting_date,
                "time_control": time_control,
                "players": players_id,
                "nb_rounds": nb_rounds,
                "description": description,
            }
        Controller().save_tournament(tournament)
        if not self.play_input():
            return False
        else:
            return True
        # On joue le tournoi
        players = self.sort_players(players)
        for i in range(nb_rounds):
            date_debut_ronde = self.date_input("Date de début de la ronde " + str(i+1) + "(format DD/MM/YYYY):\n>")

    # Inputs
    def date_input(self, display):
        while True:
            value = input(display)
            print(value)
            if self.verify_date(value):
                return value
            else:
                print("Veuillez entrer une date au format valide: DD/MM/YYYY")

    def time_control_input(self):
        while True:
            value = input("Cadence du tournoi:\n"
                          "0 - Bullet\n"
                          "1 - Blitz\n"
                          "2 - Rapide\n>")
            if value in ["0", "1", "2"]:
                return value
            else:
                print("Veuillez entrer une valeur valide")

    def nb_players_input(self):
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

    def players_input(self, nb_players):
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
                value = input(display)
                if value in assertions:
                    players.append(Controller().get_player_by_id(int(value)))
                else:
                    print("Veuillez entrer une valeur valide")
                    continue
            return players

    def nb_rounds_input(self, nb_matchs):
        while True:
            if nb_matchs == 1:
                return 1
            else:
                value = input("Nombre de tour :\n>")
                if value.isnumeric():
                    if 0 < int(value) <= nb_matchs:
                        return int(value)
                    else:
                        print("Veuillez entrer une valeur entre 1 et " + nb_matchs)
                else:
                    print("Veuillez entrer une valeur numérique valide.")

    def play_input(self):
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

    # Sorting
    def players_sorted(self, players):
        sorted = True
        for i in range(len(players) - 1):
            if players[i].rank > players[i + 1].rank:
                sorted = False
        return sorted

    def sort_players(self, players):
        while not self.players_sorted(players):
            for i in range(len(players) - 1):
                if players[i].rank > players[i + 1].rank:
                    temp = players[i]
                    players[i] = players[i + 1]
                    players[i + 1] = temp
        return players
    ###################################################################################################################

    def get_matchs(self, players, nb_matchs):
        pairs = []
        for i in range(nb_matchs):
            pairs.append({players[i], players[i+nb_matchs]})
