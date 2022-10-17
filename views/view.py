from tkinter import *

class View(Tk):
    def __init__(self):
        super().__init__()
        self.wm_protocol("WM_DELETE_WINDOW", exit)
        self.resizable(False, False)
        self.title("Tournoi d'échec")

    #Getters
    @property
    def h1_font(self):
        return ("Helvetica", 14, "bold")

    @property
    def h2_font(self):
        return ("Helvetica", 11, "bold")