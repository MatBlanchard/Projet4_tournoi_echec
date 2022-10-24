

class Match:
    def __init__(self, id, players, scores):
        self.id = id
        self.players = players
        self.scores = scores

    def serialized(self):
        players_id = []
        for p in self.players:
            players_id.append(p.id)
        return {
            "id": self.id,
            "players": players_id,
            "scores": self.scores,
        }