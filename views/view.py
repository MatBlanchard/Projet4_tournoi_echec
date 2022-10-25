from datetime import *


class View:
    @staticmethod
    def get_date(value):
        if "-" not in value:
            raise ValueError("Expected format : DD-MM-YYYY")
        values = value.split("-")
        return date(int(values[2]), int(values[1]), int(values[0]))

    @staticmethod
    def verify_hour(hour):
        if ":" not in hour:
            return False
        else:
            hour = hour.split(":")
            if len(hour) != 2:
                return False
            for h in hour:
                if not h.isnumeric():
                    return False
            if int(hour[0]) < 0 or int(hour[1]) < 0:
                return False
            if int(hour[0]) > 23 or int(hour[1]) > 59:
                return False
            return True

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
