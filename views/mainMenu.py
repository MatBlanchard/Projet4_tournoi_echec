from tkinter import *
from controllers.controller import Controller
from views.view import View

class MainMenu(View):
    def __init__(self):
        super().__init__()
        Label(self, text="Page d'acceuil", font=self.h1_font).pack()
        Button(self, text="Gestion des tournois", command=lambda:Controller().go_to_tournament_view(self)).pack(side=LEFT, expand=True)
        Button(self, text="Gestion des joueurs", command=lambda:Controller().go_to_player_view(self)).pack(side=LEFT, expand=True)




