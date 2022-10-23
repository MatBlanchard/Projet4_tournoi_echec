import os
from tinydb import TinyDB

from models.player import Player
from models.singleton import Singleton


class DAO(metaclass=Singleton):
    def __init__(self):
        self.database = TinyDB("data/database.json")
        self.playerDB = self.database.table("players")

    def save(self, table_name, data):
        if not os.path.exists("data"):
            os.mkdir("data")
        self.database.table(table_name).insert(data)

    def load_players(self):
        players = []
        for p in self.playerDB:
            players.append(Player(p["id"], p["name"], p["first_name"], p["date_of_birth"], p["sex"], p["rank"]))
        return players
