class Tournament:
    def __init__(self, name, place, date, time_control, players, nb_rounds=4, description=""):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.description = description
