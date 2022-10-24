from controllers.controller import Controller
from models.round import Round
from views.view import View
from models.singleton import Singleton
from models.match import Match
from datetime import *


class LoadTournament(View, metaclass=Singleton):
    def show(self, tournament):
        players = self.sort_players(tournament.players)
        nb_matchs = int(len(tournament.players)/2)
        for i in range(tournament.nb_rounds):
            name = "Ronde " + str(i+1)
            starting_date = datetime.now
            Controller().create_round(tournament, name, starting_date)
            for j in range(nb_matchs):
                joueurs = self.get_pair(players, j, nb_matchs)
                scores = self.score_input(j)

    @staticmethod
    def score_input(match_num):
        while True:
            value = input("Score match " + match_num + ":\n"
                          "0 - [1:0]"
                          "1 - [0.5:0.5]"
                          "2 - [0:1]"
                          )
            if value in ["0", "1", "2"]:
                if value == "0":
                    return [1,0]
                elif value == "1":
                    return [0.5, 0.5]
                elif value == "2":
                    return [0, 1]
            else:
                print("Veuillez entrer une valeur valide")

    # Sorting
    def players_sorted(self, players):
        for i in range(len(players) - 1):
            if players[i].rank < players[i + 1].rank:
                return False
        return True

    def sort_players(self, players):
        while not self.players_sorted(players):
            for i in range(len(players) - 1):
                if players[i].rank < players[i + 1].rank:
                    temp = players[i]
                    players[i] = players[i + 1]
                    players[i + 1] = temp
        return players
    #####################################################
    def get_pair(self, players, match_num, nb_matchs):
        return [players[match_num], players[match_num+nb_matchs]]

    def create_match(self, players, scores):
        from controllers.controller import Controller
        match = Match(len(Controller().matchs)+1, players, scores)
        Controller().matchs.append(match)
        serialized_match = {
            "id": len(Controller().matchs),
            "players": players,
            "scores": scores
        }
        Controller().save("matchs", serialized_match)
