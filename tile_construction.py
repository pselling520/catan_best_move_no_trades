class Tile:
    def __init__(self, neighboring_land_tiles, neighboring_water_tiles,
                 roll_number, has_thief):
        self.neighboring_land_tiles = neighboring_land_tiles
        self.neighboring_water_tiles = neighboring_water_tiles
        self.roll_number = roll_number
        self.has_thief = has_thief
