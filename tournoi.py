class Tournoi:
    def __init__(self, nom, lieu, date):
        self.setNom(nom)
        self.setLieu(lieu)
        self.setDate(date)
        self.setTour(4)

    #Setters
    def setNom(self, nom):
        self.nom = nom

    def setLieu(self, lieu):
        self.lieu = lieu

    def setDate(self, date):
        self.date = date

    def setTour(self, tour):
        self.tour = tour

    #Getters
    def getNom(self):
        return self.nom

    def getLieu(self):
        return self.lieu

    def getDate(self):
        return self.date

    def getTour(self):
        return self.tour

    def __str__(self):
        return "[nom: " + self.getNom() + " | lieu: " + self.getLieu() + " | date: " + str(self.getDate()) + " | tour: " + str(self.getTour()) + "]"
