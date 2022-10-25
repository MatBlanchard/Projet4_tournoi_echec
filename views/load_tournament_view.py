from views.view import View
from models.singleton import Singleton
from datetime import *


class LoadTournament(View, metaclass=Singleton):
    def show(self, tournament):
        from controllers.controller import Controller
        if tournament.ending_date.year == 1:
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
            self.update_rank(tournament.players)

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
            value = input(round_name.capitalize() + ": " + players_pair[0].name + " (" + str(players_pair[0].rank) + ") "
                          "vs " + players_pair[1].name + " (" + str(players_pair[1].rank) + ")\n"
                          "Jouer le match? (Y/N) \n>")
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

    @staticmethod
    def update_rank_input():
        while True:
            value = input("Mettre à jour les classements des joueurs? (Y/N) \n>")
            if value in ["y", "Y", "n", "N"]:
                return value
            else:
                print("Veuillez entrer Y ou N")

    @staticmethod
    def rank_input(player):
        while True:
            value = input("Joueur:" + player.first_name + " " + player.name + "\n"
                          "Nouveau classement:\n>")
            if value.isnumeric():
                if int(value) > 0:
                    return int(value)
                else:
                    print("Veuillez entrer une valeur supérieure à 0")
            else:
                print("Veuillez entrer une valeur numérique valide.")
    ####################################################################################################################

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
        if round.ending_datetime.year == 1:
            round.ending_datetime = datetime.now()
            Controller().update("rounds", round.serialized())
            if self.display_round_result(round) == "quit":
                return "quit"

    def display_round_result(self, round):
        print("Résultats " + round.name + " | début: " + round.starting_datetime.strftime("%d-%m-%Y %H:%M") +
              " | fin: " + round.ending_datetime.strftime("%d-%m-%Y %H:%M"))
        for m in round.matchs:
            print(m)
        if self.continue_input() in ["n", "N"]:
            return "quit"

    def display_tournament_result(self, tournament):
        print("Résultats " + tournament.name + " | début: " + tournament.starting_date.strftime("%d-%m-%Y") +
              " | fin: " + tournament.ending_date.strftime("%d-%m-%Y"))
        for r in tournament.rounds:
            self.display_round_result(r)
        players = self.score_sort(tournament)
        print("Scores des joueurs:")
        for p in players:
            print(p.first_name + " " + p.name + ": " + str(p.get_score(tournament)))
        if self.update_rank_input() in ["n", "N"]:
            return "quit"

    def update_rank(self, players):
        from controllers.controller import Controller
        for p in players:
            p.rank = self.rank_input(p)
            Controller().update("players", p)
