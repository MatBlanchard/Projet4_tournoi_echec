from datetime import date


class View:
    @staticmethod
    def get_date(value):
        if "-" not in value:
            raise ValueError("Expected format : DD-MM-YYYY")
        values = value.split("-")
        return date(int(values[2]), int(values[1]), int(values[0]))

    @staticmethod
    def leave_input():
        while True:
            value = input("r - retour:\n>")
            if value in ["r", "R"]:
                return value
            else:
                print("Veuillez entrer r pour revenir en arriere")

    @staticmethod
    def rank_input(player):
        while True:
            value = input("Joueur: " + player.first_name + " " + player.name + " (" + str(player.rank) + ")\n"
                          "Nouveau classement:\n>")
            if value.isnumeric():
                if int(value) > 0:
                    return int(value)
                else:
                    print("Veuillez entrer une valeur supérieure à 0")
            else:
                print("Veuillez entrer une valeur numérique valide.")

    @staticmethod
    def tournament_input(display):
        from controllers.controller import Controller
        while True:
            assertions = []
            for t in Controller().tournaments:
                display += str(t) + "\n"
                assertions.append(str(t.id))
            assertions.append("r")
            assertions.append("R")
            value = input(display + "r - Retour\n>")
            if value in ["r", "R"]:
                return "quit"
            if value in assertions:
                return Controller().get_tournament_by_id(int(value))
            else:
                print("Veuillez entrer une valeur valide")
                continue

    def update_rank(self, player):
        from controllers.controller import Controller
        player.rank = self.rank_input(player)
        Controller().update("players", player.serialized())

    @staticmethod
    def display_round_result(round):
        if round.status == "in progress":
            fin = "en cours"
        else:
            fin = round.ending_datetime.strftime("%d/%m/%Y %H:%M")
        print("Résultats " + round.name + " | début: " + round.starting_datetime.strftime("%d-%m-%Y %H:%M") +
              " | fin: " + fin)
        for m in round.matchs:
            print(m)

    @staticmethod
    def id_sorted(players):
        for i in range(len(players) - 1):
            if players[i].id > players[i + 1].id:
                return False
        return True

    def id_sort(self, players):
        while not self.id_sorted(players):
            for i in range(len(players) - 1):
                if players[i].id > players[i + 1].id:
                    temp = players[i]
                    players[i] = players[i + 1]
                    players[i + 1] = temp
        return players

    # Sorting
    @staticmethod
    def rank_sorted(players):
        for i in range(len(players) - 1):
            if players[i].rank < players[i + 1].rank:
                return False
        return True

    def rank_sort(self, players):
        while not self.rank_sorted(players):
            for i in range(len(players) - 1):
                if players[i].rank < players[i + 1].rank:
                    temp = players[i]
                    players[i] = players[i + 1]
                    players[i + 1] = temp
        return players

    @staticmethod
    def score_sorted(tournament):
        for i in range(len(tournament.players) - 1):
            if tournament.players[i].get_score(tournament) < tournament.players[i+1].get_score(tournament):
                return False
            elif tournament.players[i].get_score(tournament) == tournament.players[i+1].get_score(tournament) \
                    and tournament.players[i].rank < tournament.players[i+1].rank:
                return False
        return True

    def score_sort(self, tournament):
        while not self.score_sorted(tournament):
            for i in range(len(tournament.players) - 1):
                if tournament.players[i].get_score(tournament) < tournament.players[i+1].get_score(tournament):
                    temp = tournament.players[i]
                    tournament.players[i] = tournament.players[i + 1]
                    tournament.players[i + 1] = temp
                elif tournament.players[i].get_score(tournament) == tournament.players[i + 1].get_score(tournament) \
                        and tournament.players[i].rank < tournament.players[i + 1].rank:
                    temp = tournament.players[i]
                    tournament.players[i] = tournament.players[i + 1]
                    tournament.players[i + 1] = temp
        return tournament.players

    @staticmethod
    def alphabetical_sorted(players):
        for i in range(len(players) - 1):
            if players[i].name > players[i + 1].name:
                return False
            elif players[i].name == players[i + 1].name and players[i].first_name > players[i + 1].first_name:
                return False
        return True

    def alphabetical_sort(self, players):
        while not self.alphabetical_sorted(players):
            for i in range(len(players) - 1):
                if players[i].name > players[i + 1].name:
                    temp = players[i]
                    players[i] = players[i + 1]
                    players[i + 1] = temp
                elif players[i].name == players[i + 1].name and players[i].first_name > players[i + 1].first_name:
                    temp = players[i]
                    players[i] = players[i + 1]
                    players[i + 1] = temp
        return players
