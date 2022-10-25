class Player:
    def __init__(self, id, name, first_name, dob, sex, rank=1):
        self.id = id
        self.name = name.capitalize()
        self.first_name = first_name.capitalize()
        self.dob = dob
        self.sex = sex
        self.rank = rank

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name,
            "first_name": self.first_name,
            "dob": [self.dob.year, self.dob.month, self.dob.day],
            "sex": self.sex,
            "rank": self.rank
        }

    def get_score(self, tournament):
        score = 0
        for r in tournament.rounds:
            for m in r.matchs:
                if m.players[0] == self:
                    score += m.scores[0]
                elif m.players[1] == self:
                    score += m.scores[1]
        return score
    def __str__(self):
        return str(self.id) + " - " + self.name + " | " + self.first_name
