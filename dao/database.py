import os
from tinydb import TinyDB

from models.player import Player
from models.singleton import Singleton
from models.tournament import Tournament


class DAO(metaclass=Singleton):
    def __init__(self):
        self.database = TinyDB("data/database.json")
        self.playerDB = self.database.table("players")
        self.tournamentsDB = self.database.table("tournaments")

    def save(self, table_name, data):
        if not os.path.exists("data"):
            os.mkdir("data")
        self.database.table(table_name).insert(data)

    def load_players(self):
        players = []
        for p in self.playerDB:
            players.append(Player(p["id"], p["name"], p["first_name"], p["date_of_birth"], p["sex"], p["rank"]))
        return players

    def load_tournaments(self):
        from controllers.controller import Controller
        tournaments = []
        for t in self.tournamentsDB:
            players = []
            for p in t["players"]:
                players.append(Controller().get_player_by_id(p))
            tournaments.append(Tournament(t["id"], t["name"], t["place"], t["starting_date"], players, t["nb_rounds"], t["description"]))
        return tournaments
