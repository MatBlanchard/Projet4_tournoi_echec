from tkinter import *
from controllers.controller import Controller
from views.view import View

class MainMenu(View):
    def __init__(self):
        super().__init__()
        Label(self, text="Tournoi d'échec", font=self.h1_font).grid(row=0, column=0, columnspan=2, padx=(10,10), pady=(10,0))
        Label(self, text="Que voulez-vous faire?").grid(row=1, column=0, columnspan=2, padx=(10, 10),pady=(10, 0))
        Button(self, text="Gérer les tournois", command=lambda:Controller().go_to_tournament_view(self)).grid(row=2, column=0, padx=(10,0), pady=(10,10))
        Button(self, text="Gérer des joueurs", command=lambda:Controller().go_to_player_view(self)).grid(row=2, column=1, padx=(0,10), pady=(10,10))

def main():
    MainMenu().mainloop()

if __name__=="__main__":
    main()


