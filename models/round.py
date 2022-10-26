from datetime import *


class Round:
    def __init__(self, id, name, starting_datetime,
                 ending_datetime=datetime(year=1, month=1, day=1, hour=0, minute=0), matchs=None):
        self.id = id
        self.name = name
        self.starting_datetime = starting_datetime
        if matchs is None:
            self.matchs = []
        else:
            self.matchs = matchs
        self.ending_datetime = ending_datetime

    @property
    def status(self):
        if self.ending_datetime.year == 1:
            return "in progress"
        else:
            return "finished"

    def serialized(self):
        matchs_id = []
        for m in self.matchs:
            matchs_id.append(m.id)
        return {
            "id": self.id,
            "name": self.name,
            "starting_datetime": [self.starting_datetime.year,
                                  self.starting_datetime.month,
                                  self.starting_datetime.day,
                                  self.starting_datetime.hour,
                                  self.starting_datetime.minute],
            "matchs": matchs_id,
            "ending_datetime": [self.ending_datetime.year,
                                self.ending_datetime.month,
                                self.ending_datetime.day,
                                self.ending_datetime.hour,
                                self.ending_datetime.minute],
        }

    def has_played(self, player):
        for m in self.matchs:
            if player in m.players:
                return True
        return False

    def __str__(self):
        if self.status == "in progress":
            fin = "en cours"
        else:
            fin = self.ending_datetime.strftime("%d/%m/%Y %H:%M")
        return (str(self.id) + " - " + self.name.capitalize() + " | début: "
                + self.starting_datetime.strftime("%d/%m/%Y %H:%M") + " | fin: " + fin)
