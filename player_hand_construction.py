class Player:
    def __init__(self, color, victory_points = 0, owned_roads = [], owned_settlements = 0, owned_cities = 0,
                 army_size = 0, knight_cards = 0, monopoly_cards = 0, road_building_cards = 0,
                 year_of_plenty_cards = 0, victory_point_cards = 0,
                 lumber_cards = 0, brick_cards = 0, wool_cards = 0, grain_cards = 0, ore_cards = 0, hand_size = 0
                 has_longest_road = 0, has_biggest_army = 0):

        self.color = color
        self.victory_points = victory_points
        self.owned_roads = owned_roads
        self.owned_settlements = owned_settlements
        self.owned_cities = owned_cities
        self.army_size = army_size

        self.knight_cards = knight_cards
        self.monopoly_cards = monopoly_cards
        self.road_building_cards = road_building_cards
        self.year_of_plenty_cards = year_of_plenty_cards
        self.victory_point_cards = victory_point_cards

        self.lumber_cards = lumber_cards
        self.brick_cards = brick_cards
        self.wool_cards = wool_cards
        self.grain_cards = grain_cards
        self.ore_cards = ore_cards
        self.hand_size = hand_size

        self.has_longest_road = has_longest_road
        self.has_biggest_army = has_biggest_army

    def create_player(self, color):
        self.color = color

    def calculate_victory_points(self, victory_points, owned_settlements, owned_cities,
                                 victory_point_cards, has_biggest_army, has_longest_road):
        self.victory_points += victory_points + owned_settlements + 2*owned_cities + victory_point_cards + 2*has_biggest_army + 2*has_longest_road

    def calculate_hand_size(self, hand_size, lumber_cards, brick_cards, wool_cards, grain_cards, ore_cards):
        self.hand_size = lumber_cards + brick_cards + wool_cards + grain_cards + ore_cards
