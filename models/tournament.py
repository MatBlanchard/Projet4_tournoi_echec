class Tournament:
    def __init__(self, id, name, place, starting_date, time_control, players, nb_rounds=4, description="", rounds=[]):
        self.id = id
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.time_control = time_control
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.description = description
        self.is_finished = False

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
            "starting_date": [self.starting_date.year, self.starting_date.month, self.starting_date.day],
            "time_control": self.time_control,
            "players": players_id,
            "nb_rounds": self.nb_rounds,
            "description": self.description,
            "rounds": rounds_id
        }

    def __str__(self):
        return str(self.id) + " - " + self.name + " | " + self.place
