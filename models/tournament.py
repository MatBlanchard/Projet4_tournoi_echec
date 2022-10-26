from datetime import *


class Tournament:
    def __init__(self, id, name, place, starting_date, time_control, players, nb_rounds=4, description="", rounds=None,
                 ending_date=date(year=1, month=1, day=1)):
        self.id = id
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.time_control = time_control
        self.players = players
        self.nb_rounds = nb_rounds
        self.description = description
        if rounds is None:
            self.rounds = []
        else:
            self.rounds = rounds
        self.ending_date = ending_date

    @property
    def status(self):
        if self.ending_date.year == 1:
            return "in progress"
        else:
            return "finished"

    def serialized(self):
        players_id = []
        for p in self.players:
            players_id.append(p.id)
        rounds_id = []
        for r in self.rounds:
            rounds_id.append(r.id)
        return {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "starting_date": [self.starting_date.year,
                              self.starting_date.month,
                              self.starting_date.day],
            "time_control": self.time_control,
            "players": players_id,
            "nb_rounds": self.nb_rounds,
            "description": self.description,
            "rounds": rounds_id,
            "ending_date": [self.ending_date.year,
                            self.ending_date.month,
                            self.ending_date.day]
        }


    def has_played(self, player1, player2):
        for r in self.rounds:
            for m in r.matchs:
                if (player1 in m.players) and (player2 in m.players):
                    return True
        return False

    def __str__(self):
        return str(self.id) + " - " + self.name + " | " + self.place
