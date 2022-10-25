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

    def __str__(self):
        return str(self.id) + " - " + self.name + " | " + self.first_name
