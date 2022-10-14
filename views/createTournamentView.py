from views.mainMenu import *
from views.view import View

class CreateTournamentView(View):
    def __init__(self):
        super().__init__()
        Button(self, text="Retour", command=lambda:self.navigate("MainMenu")).grid(row=0, column=0)

    def navigate(self, page):
        from views.mainMenu import MainMenu
        self.destroy()
        if page == "MainMenu":
            MainMenu().deiconify()


