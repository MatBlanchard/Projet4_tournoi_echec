from datetime import *


class Round:
    def __init__(self, id, name, starting_datetime, ending_datetime=None, matchs=None):
        self.id = id
        self.name = name
        self.starting_datetime = starting_datetime
        if matchs is None:
            self.matchs = []
        if ending_datetime is None:
            self.ending_datetime = datetime(year=1, month=1, day=1, hour=0, minute=0)

    def serialized(self):
        matchs_id = []
        for m in self.matchs:
            matchs_id.append(m.id)
        return {
            "id": self.id,
            "name": self.name,
            "starting_date": [self.starting_datetime.year,
                              self.starting_datetime.month,
                              self.starting_datetime.day,
                              self.starting_datetime.hour,
                              self.starting_datetime.minute],
            "matchs": matchs_id,
            "ending_date": [self.ending_datetime.year,
                            self.ending_datetime.month,
                            self.ending_datetime.day,
                            self.ending_datetime.hour,
                            self.ending_datetime.minute],
        }
