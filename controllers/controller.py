from models.singleton import Singleton
from dao.database import DAO
from views.main_menu import MainMenu


class Controller(metaclass=Singleton):
    def __init__(self):
        self.players = DAO().load_players()

    def start(self):
        MainMenu().show()

    def save_player(self, data):
        DAO().save("player", data)

    def get_player_by_id(self, nb: int):
        for p in self.players:
            if p.id == nb:
                return p

