class Tile:
    def __init__(self, id, roll_number, has_thief, resource,
                 road1, road2, road3, road4, road5, road6,
                 vertex1, vertex2, vertex3, vertex4, vertex5, vertex6):

        self.id = id
        self.roll_number = roll_number
        self.has_thief = has_thief
        self.resource = resource

        self.road1 = road1
        self.road2 = road2
        self.road3 = road3
        self.road4 = road4
        self.road5 = road5
        self.road6 = road6

        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.vertex4 = vertex4
        self.vertex5 = vertex5
        self.vertex6 = vertex6

available_tile_roll_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

import numpy as np

def set_tile_roll_number():
    return available_tile_roll_numbers.pop(np.random.randint(1, len(available_tile_roll_numbers)+1)))
