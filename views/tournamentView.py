from views.mainMenu import *
from views.view import View

class TournamentView(View):
    def __init__(self):
        super().__init__()
        Button(self, text="Retour", command=lambda:Controller().go_to_main_menu(self)).grid(row=0, column=0)



