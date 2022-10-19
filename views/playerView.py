from controllers.controller import Controller
from tkinter import *
from views.view import View

class PlayerView(View):
    def __init__(self):
        super().__init__()
        Button(self, text="Retour", command=lambda:Controller().go_to_main_menu(self)).grid(row=0, column=0, padx=(10,0), pady=(10,10))
        Label(self, text="Gestion des joueurs", font=self.h1_font).grid(row=0, column=1, columnspan=2, padx=(10,10), pady=(10,10))
        Button(self, text="Inscrire un joueur", command=lambda:Controller().go_to_create_player_view(self)).grid(row=0, column=3, columnspan=2, padx=(0,10), pady=(10,10))
        Label(self, text="Nom", font=self.h2_font).grid(row=1, column=0, padx=(10, 10),pady=(0, 10))
        Label(self, text="Prenom", font=self.h2_font).grid(row=1, column=1, padx=(10, 10), pady=(0, 10))
        Label(self, text="Date de naissance", font=self.h2_font).grid(row=1, column=2, padx=(10, 10), pady=(0, 10))
        Label(self, text="Sexe", font=self.h2_font).grid(row=1, column=3, padx=(10, 10), pady=(0, 10))
        Label(self, text="Classement", font=self.h2_font).grid(row=1, column=4, padx=(10, 10), pady=(0, 10))
        i=2
        for j in Controller().joueurs:
            Label(self, text=j.nom).grid(row=i, column=0)
            Label(self, text=j.prenom).grid(row=i, column=1)
            Label(self, text=j.date_naissance.strftime("%d/%m/%Y")).grid(row=i, column=2)
            Label(self, text=j.sexe.name).grid(row=i, column=3)
            Label(self, text=j.classement).grid(row=i, column=4)
            i += 1
