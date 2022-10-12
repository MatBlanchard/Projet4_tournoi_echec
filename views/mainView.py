from tkinter import *
from views import createTournamentView
from views import loadTournamentView
from views import playerView

def show(window):
    if window != "firstlaunch":
        window.destroy()
    window = Tk()
    window.resizable(False, False)
    window.title("Chess tournament")
    Label(window, text="Que voulez-vous faire?").pack()
    Button(window, text="Créer un tournoi", command=createTournamentView.show()).pack(side=LEFT, expand=True)
    Button(window, text="Charger un tournoi", command=loadTournamentView.show()).pack(side=LEFT, expand=True)
    Button(window, text="Inscrire un joueur", command=playerView.show()).pack(side=LEFT, expand=True)
    window.mainloop()

def main():
    pass

if __name__=="__main__":
    main()
