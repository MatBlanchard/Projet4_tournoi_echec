from views.mainMenu import *
from views.view import View

class CreateTournamentView(View):
    def __init__(self):
        super().__init__()
        Button(self, text="Retour", command=lambda:Controller().go_to_tournament_view(self)).grid(sticky=W, row=0, column=0, padx=(10,0), pady=(10,0))
        Label(self, text="Création d'un tournoi", font=self.h1_font).grid(row=0, column=1, columnspan=3, padx=(0,10), pady=(10,0))