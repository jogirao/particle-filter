class Map:
    def __init__(self, map, obstacles):
        self.borders = Region(map)
        self.obstacles = [Region(obstacle) for obstacle in obstacles]

    def shift(self, x_i, y_i, x_f, y_f):
        pass

    def contains(self, x, y):
        pass


