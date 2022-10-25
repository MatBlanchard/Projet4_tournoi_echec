from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from models.singleton import Singleton
from views.main_menu import MainMenu
import os
from tinydb import TinyDB, where
from datetime import *


class Controller(metaclass=Singleton):
    def __init__(self):
        # Chargement des databases
        self.database = TinyDB("data/database.json")
        self.playerDB = self.database.table("players")
        self.matchDB = self.database.table("matchs")
        self.roundDB = self.database.table("rounds")
        self.tournamentDB = self.database.table("tournaments")
        ########################
        self.players = self.load_players()
        self.matchs = self.load_matchs()
        self.rounds = self.load_rounds()
        self.tournaments = self.load_tournaments()

    def start(self):
        MainMenu().show()

    def save(self, table_name, data):
        if not os.path.exists("data"):
            os.mkdir("data")
        self.database.table(table_name).insert(data)

    def update(self, table_name, data):
        self.database.table(table_name).update(
            data,
            where('id') == data['id']
        )

    # Sauvegarde et chargement des joueurs
    def create_player(self, name, first_name, dob, sex, rank):
        player = Player(len(self.players) + 1, name, first_name, dob, sex, rank)
        self.players.append(player)
        print("joueur: " + player.first_name + " " + player.name + " crée avec succès")
        self.save("players", player.serialized())
        print("joueur: " + player.first_name + " " + player.name + " sauvegardé avec succès")

    def load_players(self):
        players = []
        for p in self.playerDB:
            players.append(Player(id=p["id"],
                                  name=p["name"],
                                  first_name=p["first_name"],
                                  dob=date(p["dob"][0],
                                           p["dob"][1],
                                           p["dob"][2]),
                                  sex=p["sex"],
                                  rank=p["rank"]))
        return players

    def get_player_by_id(self, id: int):
        for p in self.players:
            if p.id == id:
                return p

    ####################################################################################################################

    # Sauvegarde et chargement des matchs
    def create_match(self, round, players, scores):
        match = Match(len(self.matchs) + 1, players, scores)
        self.matchs.append(match)
        Controller().save("matchs", match.serialized())
        round.matchs.append(match)
        Controller().update("rounds", round.serialized())

    def load_matchs(self):
        matchs = []
        for m in self.matchDB:
            players = []
            for p in m["players"]:
                players.append(self.get_player_by_id(p))
            matchs.append(Match(id=m["id"],
                                players=players,
                                scores=m["scores"]))
        return matchs

    def get_match_by_id(self, id: int):
        for m in self.matchs:
            if m.id == id:
                return m

    ####################################################################################################################

    # Sauvegarde et chargement des rondes
    def create_round(self, tournament, name, starting_date):
        round = Round(len(self.rounds) + 1, name, starting_date)
        self.rounds.append(round)
        Controller().save("rounds", round.serialized())
        tournament.rounds.append(round)
        Controller().update("tournaments", tournament.serialized())
        return round

    def load_rounds(self):
        rounds = []
        for r in self.roundDB:
            matchs = []
            for m in r["matchs"]:
                matchs.append(self.get_match_by_id(m))
            rounds.append(Round(id=r["id"],
                                name=r["name"],
                                starting_datetime=datetime(year=r["starting_datetime"][0],
                                                           month=r["starting_datetime"][1],
                                                           day=r["starting_datetime"][2],
                                                           hour=r["starting_datetime"][3],
                                                           minute=r["starting_datetime"][4]),
                                ending_datetime=datetime(year=r["ending_datetime"][0],
                                                         month=r["ending_datetime"][1],
                                                         day=r["ending_datetime"][2],
                                                         hour=r["ending_datetime"][3],
                                                         minute=r["ending_datetime"][4]),
                                matchs=matchs))
        return rounds

    def get_round_by_id(self, id: int):
        for p in self.rounds:
            if p.id == id:
                return p

    ####################################################################################################################

    # Sauvegarde et chargement des Tournois
    def create_tournament(self, name, place, starting_date, time_control, players, nb_rounds, description):
        tournament = Tournament(len(self.tournaments) + 1, name, place, starting_date,
                                time_control, players, nb_rounds, description)
        self.tournaments.append(tournament)
        self.save("tournaments", tournament.serialized())

    def load_tournaments(self):
        tournaments = []
        for t in self.tournamentDB:
            rounds = []
            for r in t["rounds"]:
                rounds.append(self.get_round_by_id(r))
            players = []
            for p in t["players"]:
                players.append(self.get_player_by_id(p))
            tournaments.append(Tournament(id=t["id"],
                                          name=t["name"],
                                          place=t["place"],
                                          starting_date=date(year=t["starting_date"][0],
                                                             month=t["starting_date"][1],
                                                             day=t["starting_date"][2]),
                                          ending_date=date(year=t["ending_date"][0],
                                                           month=t["ending_date"][1],
                                                           day=t["ending_date"][2]),
                                          time_control=t["time_control"],
                                          players=players,
                                          nb_rounds=t["nb_rounds"],
                                          description=t["description"],
                                          rounds=rounds))
        return tournaments

    def get_tournament_by_id(self, id: int):
        for t in self.tournaments:
            if t.id == id:
                return t
    ####################################################################################################################
