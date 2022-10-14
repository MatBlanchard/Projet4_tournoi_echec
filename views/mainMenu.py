from tkinter import *
from views.view import View

class MainMenu(View):
    def __init__(self):
        super().__init__()
        Label(self, text="Que voulez-vous faire?").pack()
        Button(self, text="Créer un tournoi", command=lambda:self.navigate("CreateTournamentView")).pack(side=LEFT, expand=True)
        Button(self, text="Charger un tournoi").pack(side=LEFT, expand=True)
        Button(self, text="Inscrire un joueur").pack(side=LEFT, expand=True)

    def navigate(self, page):
        from views.createTournamentView import CreateTournamentView
        self.destroy()
        if page == "CreateTournamentView":
            CreateTournamentView().deiconify()

