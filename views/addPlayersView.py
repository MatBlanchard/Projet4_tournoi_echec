from controllers.controller import Controller
from tkinter import *
from views.view import View

class AddPlayersView(View):
    def __init__(self, tournament):
        super().__init__()
        self.joueurs = [""] * 8
        self.joueurs_str = []
        self.joueurs_OM = []
        Button(self, text="Retour", command=lambda: Controller().go_to_tournament_view(self)).grid(row=0, column=0,padx=(10, 0),pady=(10, 10))
        Label(self, text="Tournoi : " + tournament.nom, font=self.h1_font).grid(row=0, column=2, columnspan=2, padx=(10, 10), pady=(10, 10))
        for i in range(8):
            self.joueurs_str.append(StringVar())
            Label(self, text="Joueur n°" + str(i+1) + " :").grid(sticky=W, row=i+1, column=0, padx=(10,0))
            self.joueurs_OM.append(OptionMenu(self, self.joueurs_str[i], *Controller().joueurs, command=lambda x,j=i:self.update_joueurs(x,j)))
            self.joueurs_OM[i].config(width=50)
            self.joueurs_OM[i].grid(sticky=W, row=i+1, column=1, columnspan=2, padx=(0,10))
        Button(self, text="Valider", command=lambda:self.add_joueurs(tournament)).grid(row=9, column=1,padx=(10, 0),pady=(10, 10))


    #Getters
    @property
    def joueurs(self):
        return self.__joueurs

    @property
    def joueurs_str(self):
        return self.__joueurs_str

    @property
    def joueurs_OM(self):
        return self.__joueurs_OM

    #Setters
    @joueurs.setter
    def joueurs(self, joueurs):
        self.__joueurs = joueurs

    @joueurs_str.setter
    def joueurs_str(self, joueurs_str):
        self.__joueurs_str = joueurs_str

    @joueurs_OM.setter
    def joueurs_OM(self, joueurs_OM):
        self.__joueurs_OM = joueurs_OM

    #Méthodes
    def update_joueurs(self, joueur, j):
        for i in self.joueurs_str:
            if str(joueur) == i.get() and self.joueurs_str.index(i) != j:
                i.set("")
        self.joueurs[j] = joueur

    def nb_error(self):
        print(self.joueurs_str[0].get() == "")
        return 1

    def add_joueurs(self, tournament):
        if self.nb_error() == 0:
            tournament.joueurs = self.joueurs
            Controller().go_to_tournament_view(self)
