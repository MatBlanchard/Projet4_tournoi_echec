from views.view import View
from models.singleton import Singleton
from datetime import *


class LoadTournament(View, metaclass=Singleton):
    def show(self, tournament):
        from controllers.controller import Controller
        if tournament.ending_date.year != 1:
            players = self.rank_sort(tournament.players)
            nb_matchs = int(len(tournament.players) / 2)
            for i in range(tournament.nb_rounds):
                if len(tournament.rounds) == (i + 1):
                    name = "ronde " + str(i + 1)
                    user_input = self.round_input(name)
                    if user_input in ["n", "N"]:
                        return
                    starting_date = datetime.now()
                    round = Controller().create_round(tournament, name, starting_date)
                    for j in range(nb_matchs):
                        if len(round.matchs) == (j + 1):
                            players_pair = self.get_pair(tournament, players, j, nb_matchs)
                            user_input = self.match_input(name)
                            if user_input in ["n", "N"]:
                                return
                            scores = self.score_input(players_pair)
                            Controller().create_match(round, players_pair, scores)
                    round.ending_datetime = datetime.now()
                    Controller().update("rounds", round.serialized())
                elif len(tournament.rounds) > (i + 1):
                    round = tournament.rounds[i]
                    for j in range(nb_matchs):
                        if len(round.matchs) == (j + 1):
                            players_pair = self.get_pair(tournament, players, j, nb_matchs)
                            user_input = self.match_input(round.name)
                            if user_input in ["n", "N"]:
                                return
                            scores = self.score_input(players_pair)
                            Controller().create_match(round, players_pair, scores)
                    round.ending_datetime = datetime.now()
                    Controller().update("rounds", round.serialized())
            tournament.ending_date = date.today()
            Controller().update("tournaments", tournament.serialized())

        else:
            print("tournoi terminé")

    @staticmethod
    def score_input(players_pair):
        while True:
            value = input("Score du match  " + players_pair[0].name + " (" + str(players_pair[0].classement) + ") "
                          "vs "+ players_pair[1].name + " (" + str(players_pair[1].classement) + "):\n"
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
            if value == ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")

    @staticmethod
    def match_input(players_pair):
        while True:
            value = input("Jouer le match " + players_pair[0].name + " (" + str(players_pair[0].classement) + ") "
                          "vs "+ players_pair[1].name + " (" + str(players_pair[1].classement) + ") (Y/N) :\n>")
            if value == ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")
    ####################################################################################################################

    @staticmethod
    def get_pair(tournament, players, match_num, nb_matchs):
        for i in range(nb_matchs):
            opponent_num = match_num + nb_matchs + i
            if opponent_num < len(players):
                if not tournament.has_played_together(players[match_num], players[opponent_num]):
                    return [players[match_num], players[opponent_num]]
            else:
                opponent_num = len(players) - opponent_num + match_num
                if not tournament.has_played_together(players[match_num], players[opponent_num]):
                    return [players[match_num], players[opponent_num]]
