from controllers.controller import Controller
from tkinter import *
from models.tournoi import Tournoi
from views.view import View

class LoadTournamentView(View):
    def __init__(self, tournament):
        super().__init__()
        Button(self, text="Retour", command=lambda: Controller().go_to_tournament_view(self)).grid(row=0, column=0,padx=(10, 0),pady=(10, 10))
        Label(self, text="Tournoi : " + tournament.nom, font=self.h1_font).grid(row=0, column=2, columnspan=2, padx=(10, 10), pady=(10, 10))
        Label(self, text="Ronde 1 :", font=self.h2_font).grid(row=1, column=0, padx=(10, 10), pady=(0, 10))
        self.sort_joueurs(tournament)
        i=2
        for j in tournament.joueurs:
            Label(self, text=j).grid(row=i, column=0)
            Label(self, text=j.classement).grid(row=i, column=1)
            i += 1

    def joueurs_sorted(self, tournament):
        sorted = True
        for i in range(len(tournament.joueurs)-1):
            if tournament.joueurs[i].classement < tournament.joueurs[i+1].classement:
                sorted = False
        return sorted

    def sort_joueurs(self, tournament):
        while not self.joueurs_sorted(tournament):
            for i in range(len(tournament.joueurs) - 1):
                if tournament.joueurs[i].classement < tournament.joueurs[i+1].classement:
                    temp = tournament.joueurs[i]
                    tournament.joueurs[i] = tournament.joueurs[i+1]
                    tournament.joueurs[i+1] = temp