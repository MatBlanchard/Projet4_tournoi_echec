from datetime import *


class View:
    @staticmethod
    def get_date(value):
        if "-" not in value:
            raise ValueError("Expected format : DD-MM-YYYY")
        values = value.split("-")
        return date(int(values[2]), int(values[1]), int(values[0]))

    # Sorting
    def rank_sorted(self, players):
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

    def score_sorted(self, tournament):
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

    def alphabetical_sorted(self, players):
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
