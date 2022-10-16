from views.mainMenu import *
from views.view import View

class TournamentView(View):
    def __init__(self):
        super().__init__()
        Button(self, text="Retour", command=lambda: Controller().go_to_main_menu(self)).grid(row=0, column=0,padx=(10, 0),pady=(10, 10))
        Label(self, text="Gestion des tournois", font=self.h1_font).grid(row=0, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))
        Button(self, text="Créer un tournoi", command=lambda:Controller().go_to_create_tournament_view(self)).grid(row=0, column=3, columnspan=2, padx=(0,10), pady=(10,10))



