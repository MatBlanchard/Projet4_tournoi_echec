from datetime import date
from tinydb import TinyDB
from models.enumeration import Sexe, Cadence
from models.joueur import Joueur
from models.singleton import Singleton
from models.tournoi import Tournoi


class Controller(metaclass=Singleton):
    def __init__(self):
        self.database = TinyDB("database.json")
        self.tournamentsDB = self.database.table("tournaments")
        self.tournaments = []
        for t in self.tournamentsDB:
            self.tournaments.append(Tournoi(t["nom"], t["lieu"], date(t["annee_debut"],t["mois_debut"],t["jour_debut"]), t["tour"], Cadence[t["cadence"]], t["description"]))
        self.joueursDB = self.database.table("players")
        self.joueurs = []
        for j in self.joueursDB:
            self.joueurs.append(Joueur(j["nom"], j["prenom"], date(j["annee_naissance"],j["mois_naissance"],j["jour_naissance"]), Sexe[j["sexe"]], j["classement"]))

    #Getters
    @property
    def database(self):
        return self.__database
    @property
    def joueursDB(self):
        return self.__joueursDB

    @property
    def main_menu(self):
        return self.__main_menu

    @property
    def tournament_view(self):
        return self.__tournament_view

    @property
    def create_tournament_view(self):
        return self.__create_tournament_view

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
    @database.setter
    def database(self, database):
        self.__database = database
    @joueursDB.setter
    def joueursDB(self, joueursDB):
        self.__joueursDB = joueursDB
    @main_menu.setter
    def main_menu(self, main_menu):
        self.__main_menu = main_menu
    @tournament_view.setter
    def tournament_view(self, tournament_view):
        self.__tournament_view = tournament_view

    @create_tournament_view.setter
    def create_tournament_view(self, create_tournament_view):
        self.__create_tournament_view = create_tournament_view

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

    def go_to_create_tournament_view(self, page):
        from views.createTournamentView import CreateTournamentView
        page.destroy()
        self.create_tournament_view = CreateTournamentView()
        self.create_tournament_view.mainloop()

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

    def create_tournament(self, nom, lieu, date_debut, tour, cadence, description):
        self.tournaments.append(Tournoi(nom, lieu, date_debut, tour, cadence, description))
        self.tournamentsDB.insert(
            {"nom": nom, "lieu": lieu, "jour_debut": date_debut.day, "mois_debut": date_debut.month,
             "annee_debut": date_debut.year, "tour": tour, "cadence": cadence.name, "description": description})

    def create_player(self, nom, prenom, date_naissance, sexe, classement):
        self.joueurs.append(Joueur(nom, prenom, date_naissance, sexe, classement))
        self.joueursDB.insert(
            {"nom": nom, "prenom": prenom, "jour_naissance": date_naissance.day, "mois_naissance": date_naissance.month,
             "annee_naissance": date_naissance.year, "sexe":sexe.name, "classement":classement})


