from region import Region


class Map:
    def __init__(self, boundaries=None, obstacles=None):
        if boundaries is None:
            boundaries = [(0, 0), (0, 1), (1, 1), (1, 0)]
        self.borders = Region(boundaries)
        self.obstacles = [Region(obstacle) for obstacle in obstacles]

    def shift(self, x_i, y_i, x_f, y_f):
        pass

    def contains(self, x, y):
        pass
