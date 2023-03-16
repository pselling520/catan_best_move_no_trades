import numpy as np

#################
#               #
#   Resources   #
#               #
#################

#  Tile type 1 = lumber
#  Tile type 2 = brick
#  Tile type 3 = wool
#  Tile type 4 = grain
#  Tile type 5 = ore
#  Tile type 6 = desert

available_tiles = [1, 1, 1, 1, # 4 lumber
                   2, 2, 2,    # 3 brick
                   3, 3, 3, 3, # 4 wool
                   4, 4, 4, 4, # 4 grain
                   5, 5, 5,    # 3 ore
                   6]          # 1 desert

def get_tile_resource():
    return available_tiles.pop(np.random.randint(1, len(available_tiles)+1))

lumber_cards = 19
brick_cards = 19
wool_cards = 19
grain_cards = 19
ore_cards = 19

###################
#                 #
#   Development   #
#   Cards         #
#                 #
###################

#  Dev card type 1 = knight
#  Dev card type 2 = road building
#  Dev card type 3 = year of plenty
#  Dev card type 4 = monopoly
#  Dev card type 5 = victory point

available_dev_cards = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5]

def get_dev_card():
    return available_dev_cards.pop(np.random.randint(1, len(available_dev_cards)+1))

knight_cards = 14
road_building_cards = 2
year_of_plenty_cards = 2
monopoly_cards = 2
victory_point_cards = 5
