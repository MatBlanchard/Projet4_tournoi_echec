from models.joueur import Joueur
from models.singleton import Singleton

class Controller(metaclass=Singleton):
    def __init__(self):
        self.joueurs = []

    #Getters
    @property
    def main_menu(self):
        return self.__main_menu

    @property
    def tournament_view(self):
        return self.__tournament_view

    @property
    def player_view(self):
        return self.__player_view

    @property
    def create_player_view(self):
        return self.__create_player_view
    @property
    def joueurs(self) -> list:
        return self.__joueurs

    #Setters
    @main_menu.setter
    def main_menu(self, main_menu):
        self.__main_menu = main_menu
    @tournament_view.setter
    def tournament_view(self, tournament_view):
        self.__tournament_view = tournament_view

    @player_view.setter
    def player_view(self, player_view):
        self.__player_view = player_view

    @create_player_view.setter
    def create_player_view(self, create_player_view):
        self.__create_player_view = create_player_view

    @joueurs.setter
    def joueurs(self, joueurs:list):
        self.__joueurs = joueurs

    #Méthodes
    def start(self):
        from views.mainMenu import MainMenu
        self.main_menu = MainMenu()
        self.main_menu.mainloop()
    def go_to_main_menu(self, page):
        from views.mainMenu import MainMenu
        page.destroy()
        self.main_menu = MainMenu()
        self.main_menu.mainloop()

    def go_to_tournament_view(self, page):
        from views.tournamentView import TournamentView
        page.destroy()
        self.tournament_view = TournamentView()
        self.tournament_view.mainloop()

    def go_to_player_view(self, page):
        from views.playerView import PlayerView
        page.destroy()
        self.player_view = PlayerView()
        self.player_view.mainloop()

    def go_to_create_player_view(self, page):
        from views.createPlayerView import CreatePlayerView
        page.destroy()
        self.create_player_view = CreatePlayerView()
        self.create_player_view.mainloop()

    def create_player(self, nom, prenom, date_naissance, sexe, classement):
        self.joueurs.append(Joueur(nom, prenom, date_naissance, sexe, classement))
