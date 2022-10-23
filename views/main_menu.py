from models.singleton import Singleton
from views.tournament_view import CreateTournament
from views.view import View
from views.player_view import CreatePlayer, LoadPlayer


class MainMenu(View, metaclass=Singleton):

    def show(self):
        from controllers.controller import Controller
        while True:
            user_input = self.get_user_entry(
                    msg_display="Que voulez-vous faire ?\n"
                                "0 - Créer un tournoi\n"
                                "1 - Charger un tournoi\n"
                                "2 - Créer un joueur\n"
                                "3 - Voir les rapports\n"
                                "q - Quitter\n> ",
                    msg_error="Veuillez entrer une valeur valide",
                    value_type="selection",
                    assertions=["0", "1", "2", "3", "4", "q"]
            )
            if user_input == "0":
                if len(Controller().players) < 2:
                    print("Il faut d'abord créer au moins 2 joueurs")
                else:
                    CreateTournament().show()
            elif user_input == "2":
                Controller().save_player(CreatePlayer().show())
            elif user_input == "3":
                LoadPlayer().show()
            elif user_input == "q":
                break
