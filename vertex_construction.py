class Vertex:
    def __init__(self,
                 neighboring_resource1, neighboring_resource2, neighboring_resource3,
                 neighboring_road1, neighboring_road2, neighboring_road3,
                 has_settlement, settlement_owner, has_city, city_owner):

        self.neighboring_resource1 = neighboring_resource1
        self.neighboring_resource2 = neighboring_resource2
        self.neighboring_resource3 = neighboring_resource3

        self.neighboring_road1 = neighboring_road1
        self.neighboring_road2 = neighboring_road2
        self.neighboring_road3 = neighboring_road3

        self.has_settlement = has_settlement
        self.settlement_owner = settlement_owner

        self.has_city = has_city
        self.city_owner = city_owner
