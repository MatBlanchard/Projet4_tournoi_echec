from views.view import View
from models.singleton import Singleton


class CreateTournament(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        name = input("Nom du tournoi:\n>")
        place = input("Nom du tournoi:\n>")
        date = self.get_user_entry(
            msg_display="Date de début du tournoi (format DD/MM/YYYY):\n> ",
            msg_error="Veuillez entrer une date au format valide: DD/MM/YYYY",
            value_type="date"
        )
        time_control = self.get_user_entry(
            msg_display="Cadence du tournoi?\n> "
                        "0 - Bullet\n"
                        "1 - Blitz\n"
                        "2 - Rapide\n",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "1", "2"]
        )
        while True:
            nb_players = int(self.get_user_entry(
                msg_display="Combien de joueurs voulez-vous ajouter ?\n",
                msg_error="Veuillez entrer une valeur valide numérique valide et paire",
                value_type="even_numeric",
            ))
            if nb_players > len(Controller().players):
                print("Il n'y a que " + str(len(Controller().players)) + " dans la base de données")
                continue
            break
        display = "Quel joueur voulez-vous ajouter?\n"
        assertions = []
        for p in Controller().players:
            display += str(p) + "\n"
            assertions.append(str(p.id))
        players = []
        while len(players) < nb_players:
            user_input = int(self.get_user_entry(
                msg_display=display + ">",
                msg_error="Veuillez entrer une valeur valide",
                value_type="selection",
                assertions=assertions
            ))
            players.append(Controller().get_player_by_id(user_input))
        if nb_players == 2:
            nb_rounds = 1
        else:
            nb_rounds = self.get_user_entry(
                msg_display="Nombre de tour:\n> ",
                msg_error="Veuillez entrer une valeur numérique valide entre 1 et " + str(nb_players/2),
                value_type="embedded_numeric",
                embedment=[1, int(nb_players/2)]
            )
        description = input("Nom du tournoi:\n>")
