class Campaign:
    def __init__(self, name, dm_name, system):
        self.name = name
        self.dm_name = dm_name
        self.system = system
        self.players = []
        self.npcs = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player) 

    def add_npc(self, npc):
        self.npcs.append(npc)

    def remove_npc(self, npc):
        self.npcs.remove(npc)

    def to_dict(self):
        return {
            "campaign_name": self.name,
            "dm_name": self.dm_name,
            "system": self.system,
            "players": [player.to_dict() for player in self.players], #for JSON, make a list of dict of player object data found in player class
            "npcs": [npc.to_dict() for npc in self.npcs]
        }