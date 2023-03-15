class Tile:
    def __init__(self, neighboring_land_tiles, neighboring_water_tiles,
                 roll_number, has_thief, resource,
                 side1, side2, side3, side4, side5, side6,
                 vertex1, vertex2, vertex3, vertex4, vertex5, vertex6):
        self.neighboring_land_tiles = neighboring_land_tiles
        self.neighboring_water_tiles = neighboring_water_tiles
        self.roll_number = roll_number
        self.has_thief = has_thief
        self.resource = resource

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6

        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.vertex4 = vertex4
        self.vertex5 = vertex5
        self.vertex6 = vertex6
