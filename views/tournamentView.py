from controllers.controller import Controller
from tkinter import *
from views.view import View

class TournamentView(View):
    def __init__(self):
        super().__init__()
        Button(self, text="Retour", command=lambda: Controller().go_to_main_menu(self)).grid(row=0, column=0,padx=(10, 0),pady=(10, 10))
        Label(self, text="Gestion des tournois", font=self.h1_font).grid(row=0, column=3, columnspan=2, padx=(10, 10), pady=(10, 10))
        Button(self, text="Créer un tournoi", command=lambda:Controller().go_to_create_tournament_view(self)).grid(sticky=E, row=0, column=6, columnspan=2, padx=(0,10), pady=(10,10))
        Label(self, text="Nom", font=self.h2_font).grid(row=1, column=0, padx=(10, 10),pady=(0, 10))
        Label(self, text="lieu", font=self.h2_font).grid(row=1, column=1, padx=(10, 10), pady=(0, 10))
        Label(self, text="Date de début", font=self.h2_font).grid(row=1, column=2, padx=(10, 10), pady=(0, 10))
        Label(self, text="Date de fin", font=self.h2_font).grid(row=1, column=3, padx=(10, 10), pady=(0, 10))
        Label(self, text="Tour", font=self.h2_font).grid(row=1, column=4, padx=(10, 10), pady=(0, 10))
        Label(self, text="Cadence", font=self.h2_font).grid(row=1, column=5, padx=(10, 10), pady=(0, 10))
        Label(self, text="Description", font=self.h2_font).grid(row=1, column=6, padx=(10, 10), pady=(0, 10))
        i=2
        for t in Controller().tournaments:
            Label(self, text=t.nom).grid(row=i, column=0)
            Label(self, text=t.lieu).grid(row=i, column=1)
            Label(self, text=t.date_debut.strftime("%d/%m/%Y")).grid(row=i, column=2)
            Label(self, text=t.tour).grid(row=i, column=4)
            Label(self, text=t.cadence.name).grid(row=i, column=5)
            Label(self, text=t.description).grid(row=i, column=6)
            if t.joueurs == []:
                Button(self, text="Ajouter joueurs", command=lambda t=t: Controller().go_to_add_players_view(self, t)).grid(row=i, column=7, padx=(10, 10))
            else:
                Button(self, text="Charger le tournoi", command=lambda t=t: Controller().go_to_load_tournament_view(self, t)).grid(row=i, column=7, padx=(10, 10))
            i += 1

