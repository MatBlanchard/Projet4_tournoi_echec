from controllers.controller import Controller
from tkinter import *
from views.view import View

class AddPlayersView(View):
    def __init__(self, tournament):
        super().__init__()
        self.nb_joueurs = 8
        self.joueurs = [""] * self.nb_joueurs
        self.joueurs_str = []
        self.joueurs_OM = []
        self.errors = []
        Button(self, text="Retour", command=lambda: Controller().go_to_tournament_view(self)).grid(row=0, column=0,padx=(10, 0),pady=(10, 10))
        Label(self, text="Tournoi : " + tournament.nom, font=self.h1_font).grid(row=0, column=2, columnspan=2, padx=(10, 10), pady=(10, 10))
        for i in range(self.nb_joueurs):
            self.joueurs_str.append(StringVar())
            Label(self, text="Joueur n°" + str(i+1) + " :").grid(sticky=W, row=i+1, column=0, padx=(10,0))
            self.joueurs_OM.append(OptionMenu(self, self.joueurs_str[i], *Controller().joueurs, command=lambda x,j=i:self.update_joueurs(x,j)))
            self.joueurs_OM[i].config(width=50)
            self.joueurs_OM[i].grid(sticky=W, row=i+1, column=1, columnspan=2, padx=(0,10))
            self.errors.append(Label(self, text="", fg="#ff0000"))
            self.errors[i].grid(sticky=W, row=i+1, column=3, columnspan=2, padx=(10, 10))
        Button(self, text="Valider", command=lambda:self.add_joueurs(tournament)).grid(row=9, column=1,padx=(10, 0),pady=(10, 10))


    #Getters
    @property
    def nb_joueurs(self):
        return self.__nb_joueurs

    @property
    def joueurs(self):
        return self.__joueurs

    @property
    def joueurs_str(self):
        return self.__joueurs_str

    @property
    def joueurs_OM(self):
        return self.__joueurs_OM

    @property
    def errors(self):
        return self.__errors

    #Setters
    @nb_joueurs.setter
    def nb_joueurs(self, nb_joueurs):
        self.__nb_joueurs = nb_joueurs

    @joueurs.setter
    def joueurs(self, joueurs):
        self.__joueurs = joueurs

    @joueurs_str.setter
    def joueurs_str(self, joueurs_str):
        self.__joueurs_str = joueurs_str

    @joueurs_OM.setter
    def joueurs_OM(self, joueurs_OM):
        self.__joueurs_OM = joueurs_OM

    @errors.setter
    def errors(self, errors):
        self.__errors = errors

    #Méthodes
    def update_joueurs(self, joueur, j):
        for i in self.joueurs_str:
            if str(joueur) == i.get() and self.joueurs_str.index(i) != j:
                i.set("")
        self.joueurs[j] = joueur

    def nb_error(self):
        nb_error = 0
        for i in range(self.nb_joueurs):
            if self.joueurs_str[i].get() == "":
                self.errors[i].config(text="Veuillez sélectionner un joueur")
                nb_error += 1
            else:
                self.errors[i].config(text="")
        return nb_error

    def add_joueurs(self, tournament):
        if self.nb_error() == 0:
            tournament.joueurs = self.joueurs
            Controller().go_to_tournament_view(self)
