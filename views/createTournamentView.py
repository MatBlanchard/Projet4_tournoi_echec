from datetime import date
from tkinter import *
from controllers.controller import Controller
from models.enumeration import Cadence
from views.view import View
import calendar

class CreateTournamentView(View):
    def __init__(self):
        super().__init__()
        self.nom = StringVar()
        self.lieu = StringVar()
        self.jour_debut = StringVar()
        self.jour_debut.set(date.today().day)
        self.mois_debut = StringVar()
        self.mois_debut.set(date.today().month)
        self.annee_debut = StringVar()
        self.annee_debut.set(date.today().year)
        self.tour = StringVar()
        self.cadence = StringVar()
        self.description = StringVar()
        Button(self, text="Retour", command=lambda:Controller().go_to_tournament_view(self)).grid(sticky=W, row=0, column=0, padx=(10,0), pady=(10,0))
        Label(self, text="Création d'un tournoi", font=self.h1_font).grid(row=0, column=1, columnspan=3, padx=(0,10), pady=(10,0))

        #Champ du nom
        Label(self, text="Nom du tournoi : ").grid(sticky=W, row=1, column=0, padx=(10,0))
        nom = Entry(self, textvariable=self.nom)
        nom.focus_set()
        nom.grid(sticky=W, row=1, column=1, columnspan=2)
        self.nom_error = Label(self, text="", fg="#ff0000")
        self.nom_error.grid(sticky=W, row=1, column=3, columnspan=2, padx=(10, 10))

        #Champ du lieu
        Label(self, text="Lieu : ").grid(sticky=W, row=2, column=0, padx=(10,0))
        lieu = Entry(self, textvariable=self.lieu)
        lieu.grid(sticky=W, row=2, column=1, columnspan=2)
        self.lieu_error = Label(self, text="", fg="#ff0000")
        self.lieu_error.grid(sticky=W, row=2, column=3, columnspan=2, padx=(10, 10))

        #Champ de la date
        Label(self, text="Date de début : ").grid(sticky=W, row=3, column=0, padx=(10,0))
        jour_debut_OM = OptionMenu(self, self.jour_debut, *self.jours)
        jour_debut_OM.grid(sticky=W, row=3, column=1, padx=(0, 10))
        mois_debut_OM = OptionMenu(self, self.mois_debut, *self.mois, command=lambda x:self.update_jours(jour_debut_OM))
        mois_debut_OM.grid(sticky=W, row=3, column=2, padx=(0, 10))
        annee_debut_OM = OptionMenu(self, self.annee_debut, *self.annees, command=lambda x:self.update_jours(jour_debut_OM))
        annee_debut_OM.grid(sticky=W, row=3, column=3, padx=(0, 10))

        #Champ du tour
        Label(self, text="Nombre de tour : ").grid(sticky=W, row=4, column=0, padx=(10,0))
        tour = Entry(self, textvariable=self.tour)
        tour.grid(sticky=W, row=4, column=1, columnspan=2)
        self.tour_error = Label(self, text="", fg="#ff0000")
        self.tour_error.grid(sticky=W, row=4, column=3, columnspan=2, padx=(10, 10))

        #Champ de la cadence
        Label(self, text="Cadence : ").grid(sticky=W, row=6, column=0, padx=(10,0))
        cadenceList = Cadence.list()
        self.cadence.set(cadenceList[0])
        cadence_OM = OptionMenu(self, self.cadence, *cadenceList)
        cadence_OM.grid(sticky=W, row=6, column=1, columnspan=2, padx=(0,10))

        #Champ de la description
        Label(self, text="Description : ").grid(sticky=W, row=7, column=0, padx=(10,0))
        description = Entry(self, textvariable=self.description)
        description.grid(sticky=W, row=7, column=1, columnspan=2)
        self.description_error = Label(self, text="", fg="#ff0000")
        self.description_error.grid(sticky=W, row=7, column=3, columnspan=2, padx=(10, 10))

        #Submit
        Button(self, text="Valider", command=self.create_tournament).grid(sticky=W, row=8, column=1, pady=(10, 10))

    #Getters
    @property
    def nom(self):
        return self.__nom

    @property
    def lieu(self):
        return self.__lieu

    @property
    def jour_debut(self):
        return self.__jour_debut

    @property
    def mois_debut(self):
        return self.__mois_debut

    @property
    def annee_debut(self):
        return self.__annee_debut

    @property
    def date_debut(self):
        return date(int(self.annee_debut.get()), int(self.mois_debut.get()), int(self.jour_debut.get()))

    @property
    def tour(self):
        return self.__tour

    @property
    def cadence(self):
        return self.__cadence

    @property
    def description(self):
        return self.__description

    @property
    def month_range(self) -> int:
        return calendar.monthrange(int(self.annee_debut.get()), int(self.__mois_debut.get()))[1]

    @property
    def jours(self) -> list:
        self.__jours = []
        i = 1
        while i <= self.month_range:
            self.__jours.append(i)
            i += 1
        return self.__jours

    @property
    def mois(self) -> list:
        self.__mois = []
        i = 1
        while i != 13:
            self.__mois.append(i)
            i += 1
        return self.__mois

    @property
    def annees(self) -> list:
        self.__annees = []
        i = date.today().year
        while i != 2060:
            self.__annees.append(i)
            i += 1
        return self.__annees

    #Setters
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @lieu.setter
    def lieu(self, lieu):
        self.__lieu = lieu

    @jour_debut.setter
    def jour_debut(self, jour_debut):
        self.__jour_debut = jour_debut

    @mois_debut.setter
    def mois_debut(self, mois_debut):
        self.__mois_debut = mois_debut

    @annee_debut.setter
    def annee_debut(self, annee_debut):
        self.__annee_debut = annee_debut

    @tour.setter
    def tour(self, tour):
        self.__tour = tour

    @cadence.setter
    def cadence(self, cadence):
        self.__cadence = cadence

    @description.setter
    def description(self, description):
        self.__description = description


    #Methodes
    def update_jours(self, jour_debut):
        if int(self.jour_debut.get()) > self.month_range:
            self.jour_debut.set(self.month_range)
        jour_debut["menu"].delete(0, "end")
        for i in self.jours:
            jour_debut["menu"].add_command(label=i, command=lambda i=i:self.jour_debut.set(i))

    def nb_error(self):
        nb_error = 0
        if self.nom.get() == "" or self.lieu.get() == "" or self.tour.get() == "" or self.description.get() == "":
            if self.nom.get() == "":
                self.nom_error.config(text="Ce champ ne peut pas étre nul")
                nb_error += 1
            else:
                self.nom_error.config(text="")
            if self.lieu.get() == "":
                self.lieu_error.config(text="Ce champ ne peut pas étre nul")
                nb_error += 1
            else:
                self.lieu_error.config(text="")
            if self.tour.get() == "":
                self.tour_error.config(text="Ce champ ne peut pas étre nul")
                nb_error += 1
            else:
                self.tour_error.config(text="")
                try:
                    tour = int(self.tour.get())
                    if tour <= 0:
                        self.tour_error.config(text="Le nombre de tour doit étre > 0")
                        nb_error += 1
                except ValueError:
                    self.tour_error.config(text="Le nombre de tour doit étre un nombre")
                    nb_error += 1
            if self.description.get() == "":
                self.description_error.config(text="Ce champ ne peut pas étre nul")
                nb_error += 1
            else:
                self.description_error.config(text="")
        return nb_error
    def create_tournament(self):
        controller = Controller()
        if self.nb_error() == 0:
            print(type(self.date_debut))
            controller.create_tournament(self.nom.get(), self.lieu.get(), self.date_debut, int(self.tour.get()), Cadence[self.cadence.get()], self.description.get())
            controller.go_to_tournament_view(self)

def main():
    CreateTournamentView().mainloop()

if __name__=="__main__":
    main()
