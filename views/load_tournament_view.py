from views.view import View
from models.singleton import Singleton


class CreateTournament(View, metaclass=Singleton):
    def show(self, tournament=None):