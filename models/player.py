class Player:
    def __init__(self, id, name, first_name, date_of_birth, sex, rank=1):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return str(self.id) + " - " + self.name + " | " + self.first_name
