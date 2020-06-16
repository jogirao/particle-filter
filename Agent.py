import math


class Agent:
    def __init__(self, x, y, orientation=0):
        self.coordinates = (x, y)
        self.orientation = orientation

    def get_observations(self, map):
        pass

    def move_agent(self, map, distance, angle):
        x = distance * math.cos(angle+self.orientation) + self.coordinates[0]
        y = distance * math.sin(angle+self.orientation) + self.coordinates[1]
        self.coordinates = map.shift(*self.coordinates, x, y)
