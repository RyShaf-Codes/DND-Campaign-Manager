class Player:
    def __init__(self, player_name, character_name, character_class, level, race):
        self.player_name = player_name
        self.character_name = character_name
        self.character_class = character_class
        self.level = level
        self.race = race

    def to_dict(self):
        return {
            "player_name": self.player_name,
            "character_name": self.character_name,
            "character_class": self.character_class,
            "level": self.level,
            "race": self.race
        }