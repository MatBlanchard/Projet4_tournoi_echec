from views.view import View
from models.singleton import Singleton
from datetime import datetime, date


class LoadTournament(View, metaclass=Singleton):
    def show(self, tournament):
        from controllers.controller import Controller
        modify_ranks = False
        if tournament.status == "in progress":
            modify_ranks = True
            for i in range(tournament.nb_rounds):
                if len(tournament.rounds) == i:
                    name = "ronde " + str(i + 1)
                    user_input = self.round_input(name)
                    if user_input in ["n", "N"]:
                        return ""
                    starting_date = datetime.now()
                    round = Controller().create_round(tournament, name, starting_date)
                elif len(tournament.rounds) > i:
                    round = tournament.rounds[i]
                else:
                    break
                if self.play_round(tournament, round) == "quit":
                    return None
            tournament.ending_date = date.today()
            Controller().update("tournaments", tournament.serialized())
        if self.display_tournament_result(tournament) == "quit":
            return None
        else:
            if modify_ranks:
                if self.continue_input() in ["y", "Y"]:
                    self.update_ranks(tournament.players)

    # Inputs
    @staticmethod
    def score_input(players_pair):
        while True:
            value = input("Score du match " + players_pair[0].name + " (" + str(players_pair[0].rank) + ") "
                          "vs " + players_pair[1].name + " (" + str(players_pair[1].rank) + "):\n"
                          "0 - [1:0]\n"
                          "1 - [0.5:0.5]\n"
                          "2 - [0:1]\n>"
                          )
            if value in ["0", "1", "2"]:
                if value == "0":
                    return [1, 0]
                elif value == "1":
                    return [0.5, 0.5]
                elif value == "2":
                    return [0, 1]
            else:
                print("Veuillez entrer une valeur valide")

    @staticmethod
    def round_input(name):
        while True:
            value = input("Jouer la " + name + "? (Y/N) \n>")
            if value in ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")

    @staticmethod
    def match_input(round_name, players_pair):
        while True:
            value = input(round_name.capitalize() + ": " + players_pair[0].name + " (" +
                          str(players_pair[0].rank) + ") vs " + players_pair[1].name + " (" +
                          str(players_pair[1].rank) + ")\n"
                          "Jouer le match? (Y/N) \n>")
            if value in ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")

    @staticmethod
    def update_rank_input():
        while True:
            value = input("Mettre à jour les classements des joueurs? (Y/N) \n>")
            if value in ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")

    @staticmethod
    def continue_input():
        while True:
            value = input("Y - Continuer\n"
                          "N - Quitter\n>")
            if value in ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")
    ###################################################################################################################

    def get_pair(self, tournament, round, match_num, nb_matchs):
        if round.name == "ronde 1":
            players = self.rank_sort(tournament.players)
            return [players[match_num], players[match_num + nb_matchs]]
        else:
            players = self.score_sort(tournament)
            player_one = ""
            for p in players:
                if not round.has_played(p):
                    player_one = p
                    break
            for p in players:
                if p is not player_one:
                    if not tournament.has_played(player_one, p):
                        if not round.has_played(p):
                            return [player_one, p]
            for p in players:
                if p is not player_one:
                    if not round.has_played(p):
                        return [player_one, p]

    def play_round(self, tournament, round):
        from controllers.controller import Controller
        nb_matchs = int(len(tournament.players) / 2)
        for j in range(nb_matchs):
            if len(round.matchs) == j:
                players_pair = self.get_pair(tournament, round, j, nb_matchs)
                user_input = self.match_input(round.name, players_pair)
                if user_input in ["n", "N"]:
                    return "quit"
                scores = self.score_input(players_pair)
                Controller().create_match(round, players_pair, scores)
        if round.status == "in progress":
            round.ending_datetime = datetime.now()
            Controller().update("rounds", round.serialized())
            self.display_round_result(round)
            if self.continue_input() in ["n", "N"]:
                return "quit"

    def display_tournament_result(self, tournament):
        print("Résultats " + tournament.name + " | début: " + tournament.starting_date.strftime("%d-%m-%Y") +
              " | fin: " + tournament.ending_date.strftime("%d-%m-%Y"))
        for r in tournament.rounds:
            self.display_round_result(r)
            if self.continue_input() in ["n", "N"]:
                return "quit"
        players = self.score_sort(tournament)
        print("Scores des joueurs:")
        for p in players:
            print(p.first_name + " " + p.name + ": " + str(p.get_score(tournament)))

    def update_ranks(self, players):
        for p in players:
            self.update_rank(p)
