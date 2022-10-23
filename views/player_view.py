from models.player import Player
from models.singleton import Singleton
from views.view import View


class CreatePlayer(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        name = input("Nom du joueur:\n>")
        first_name = input("Prénom du joueur:\n>")

        date_of_birth = self.get_user_entry(
            msg_display="Date de naissance (format DD/MM/YYYY):\n> ",
            msg_error="Veuillez entrer une date au format valide: DD/MM/YYYY",
            value_type="date"
        )

        sex = self.get_user_entry(
            msg_display="Sexe (H ou F):\n> ",
            msg_error="Veuillez entrer H ou F",
            value_type="selection",
            assertions=["H", "h", "F", "f"]
        ).upper()

        rank = self.get_user_entry(
            msg_display="Classement:\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="strictly_positive_numeric"
        )
        Controller().players.append(Player(len(Controller().players)+1, name, first_name, date_of_birth, sex, rank))
        return {
            "id": len(Controller().players),
            "name": name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "sex": sex,
            "rank": rank,
        }


class LoadPlayer(View, metaclass=Singleton):
    def show(self):
        from controllers.controller import Controller
        print("Voici la liste des joueurs")
        for p in Controller().players:
            print("nom: " + p.name + " | prénom: " + p.first_name + " | date_naissance: " + p.date_of_birth
                  + " | sexe: " + p.first_name + " | classement: " + p.rank)
        self.get_user_entry(
            msg_display="r - retour:\n> ",
            msg_error="Veuillez entrer r pour quitter",
            value_type="selection",
            assertions=["r"]
        )
