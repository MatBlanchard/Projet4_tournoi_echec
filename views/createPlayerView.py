from models.enumeration import Sexe
from views.mainMenu import *
from views.view import View
from datetime import *
import calendar

class CreatePlayerView(View):
    def __init__(self):
        super().__init__()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.jour_naissance = StringVar()
        self.jour_naissance.set(date.today().day)
        self.mois_naissance = StringVar()
        self.mois_naissance.set(date.today().month)
        self.annee_naissance = StringVar()
        self.annee_naissance.set(date.today().year)
        self.sexe = StringVar()
        self.classement = StringVar()
        Button(self, text="Retour", command=lambda:Controller().go_to_player_view(self)).grid(sticky=W, row=0, column=0, padx=(10,0), pady=(10,0))
        Label(self, text="Inscription d'un joueur", font=self.h1_font).grid(row=0, column=1, columnspan=3, padx=(0,10), pady=(10,0))

        #Champ du nom
        Label(self, text="Nom : ").grid(sticky=W, row=1, column=0, padx=(10,0))
        nom = Entry(self, textvariable=self.nom)
        nom.focus_set()
        nom.grid(sticky=W, row=1, column=1, columnspan=2)
        self.nom_error = Label(self, text="", fg="#ff0000")
        self.nom_error.grid(sticky=W, row=1, column=3, columnspan=2, padx=(10, 10))

        #Champ du prenom
        Label(self, text="Prenom : ").grid(sticky=W, row=2, column=0, padx=(10,0))
        prenom = Entry(self, textvariable=self.prenom)
        prenom.grid(sticky=W, row=2, column=1, columnspan=2)
        self.prenom_error = Label(self, text="", fg="#ff0000")
        self.prenom_error.grid(sticky=W, row=2, column=3, columnspan=2, padx=(10, 10))

        #Champ de la date de naissance
        Label(self, text="Date de naissance : ").grid(sticky=W, row=3, column=0, padx=(10,0))
        jour_naissance_OM = OptionMenu(self, self.jour_naissance, *self.jours)
        jour_naissance_OM.grid(sticky=W, row=3, column=1, padx=(0, 10))
        mois_naissance_OM = OptionMenu(self, self.mois_naissance, *self.mois, command=lambda x:self.update_jours(jour_naissance_OM))
        mois_naissance_OM.grid(sticky=W, row=3, column=2, padx=(0, 10))
        annee_naissance_OM = OptionMenu(self, self.annee_naissance, *self.annees, command=lambda x:self.update_jours(jour_naissance_OM))
        annee_naissance_OM.grid(sticky=W, row=3, column=3, padx=(0, 10))

        #Champ du sexe
        Label(self, text="Sexe : ").grid(sticky=W, row=4, column=0, padx=(10,0))
        sexeList = Sexe.list()
        self.sexe.set(sexeList[0])
        sexe_OM = OptionMenu(self, self.sexe, *sexeList)
        sexe_OM.grid(sticky=W, row=4, column=1, columnspan=2, padx=(0,10))

        #Champ du classement
        Label(self, text="Classement : ").grid(sticky=W, row=5, column=0, padx=(10,0))
        classement = Entry(self, textvariable=self.classement)
        classement.grid(sticky=W, row=5, column=1, columnspan=2)
        self.classement_error = Label(self, text="", fg="#ff0000")
        self.classement_error.grid(sticky=W, row=5, column=3,columnspan=2, padx=(10, 10))

        #Submit
        Button(self, text="Valider", command=self.create_player).grid(sticky=W, row=6, column=1, pady=(10, 10))

    #Getters
    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def jour_naissance(self):
        return self.__jour_naissance

    @property
    def mois_naissance(self):
        return self.__mois_naissance

    @property
    def annee_naissance(self):
        return self.__annee_naissance

    @property
    def date_naissance(self):
        return date(int(self.annee_naissance.get()), int(self.mois_naissance.get()), int(self.jour_naissance.get()))

    @property
    def sexe(self):
        return self.__sexe

    @property
    def classement(self):
        return self.__classement

    @property
    def nom_error(self):
        return self.__nom_error

    @property
    def prenom_error(self):
        return self.__prenom_error

    @property
    def classement_error(self):
        return self.__classement_error

    @property
    def month_range(self) -> int:
        return calendar.monthrange(int(self.__annee_naissance.get()), int(self.__mois_naissance.get()))[1]

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
        while i != 1960:
            self.__annees.append(i)
            i -= 1
        return self.__annees

    #Setters
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @jour_naissance.setter
    def jour_naissance(self, jour_naissance):
        self.__jour_naissance = jour_naissance

    @mois_naissance.setter
    def mois_naissance(self, mois_naissance):
        self.__mois_naissance = mois_naissance

    @annee_naissance.setter
    def annee_naissance(self, annee_naissance):
        self.__annee_naissance = annee_naissance

    @sexe.setter
    def sexe(self, sexe):
        self.__sexe = sexe

    @classement.setter
    def classement(self, classement):
        self.__classement = classement

    @nom_error.setter
    def nom_error(self, nom_error):
        self.__nom_error = nom_error

    @prenom_error.setter
    def prenom_error(self, prenom_error):
        self.__prenom_error = prenom_error

    @classement_error.setter
    def classement_error(self, classement_error):
        self.__classement_error = classement_error

    #Méthodes
    def update_jours(self, jour_naissance):
        if int(self.jour_naissance.get()) > self.month_range:
            self.jour_naissance.set(self.month_range)
        jour_naissance["menu"].delete(0, "end")
        for i in self.jours:
            jour_naissance["menu"].add_command(label=i, command=lambda i=i:self.jour_naissance.set(i))

    def create_player(self):
        controller = Controller()
        if self.nom.get() == "" or self.prenom.get() == "" or self.classement.get() == "":
            if self.nom.get() == "":
                self.nom_error.config(text="Ce champ ne peut pas étre nul")
            else:
                self.nom_error.config(text="")
            if self.prenom.get() == "":
                self.prenom_error.config(text="Ce champ ne peut pas étre nul")
            else:
                self.prenom_error.config(text="")
            if self.classement.get() == "":
                self.classement_error.config(text="Ce champ ne peut pas étre nul")
            else:
                self.classement_error.config(text="")
        try:
            classement = int(self.classement.get())
            if classement < 0:
                self.classement_error.config(text="Le classement doit étre >= 0")
            else:
                controller.create_player(self.nom.get(), self.prenom.get(), self.date_naissance, Sexe[self.sexe.get()], classement)
                controller.go_to_player_view(self)
        except ValueError:
            if self.classement.get() != "":
                self.classement_error.config(text="Le classement doit étre un nombre")


def main():
    CreatePlayerView().mainloop()

if __name__=="__main__":
    main()