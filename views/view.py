from tkinter import *


class View(Tk):
    __instance = None

    def __new__(cls,*args, **kwargs):
        if cls.__instance is None :
            cls.__instance = super(View, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Tournoi d'échec")