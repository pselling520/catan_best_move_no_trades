class Road:
    def __init__(self, road_owner = 'Available', neighboring_resource1, neighboring_resource2,
                 neighboring_vertex1, neighboring_vertex2):

        self.road_owner = road_owner
        self.neighboring_resource1 = neighboring_resource1
        self.neighboring_resource2 = neighboring_resource2

        self.neighboring_vertex1 = neighboring_vertex1
        self.neighboring_vertex2 = neighboring_vertex2
