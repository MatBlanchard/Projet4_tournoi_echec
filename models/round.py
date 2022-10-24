class Round:
    def __init__(self, id, name, starting_date, matchs=[]):
        self.id = id
        self.name = name
        self.starting_date = starting_date
        self.matchs = matchs

    def serialized(self):
        matchs_id = []
        for m in self.matchs:
            matchs_id.append(m.id)
        return {
            "id": self.id,
            "name": self.name,
            "starting_date": self.starting_date,
            "matchs": matchs_id
        }
