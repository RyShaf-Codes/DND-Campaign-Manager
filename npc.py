class NPC:
    def __init__(self, npc_name, npc_level, npc_race, npc_class):
        self.npc_name = npc_name
        self.npc_level = npc_level
        self.npc_class = npc_class
        self.npc_race = npc_race

    def to_dict(self):
        return {
            "npc_name": self.npc_name,
            "npc_level": self.npc_level,
            "npc_class": self.npc_class,
            "npc_race": self.npc_race,
        }



