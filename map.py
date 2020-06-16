from region import Region
import heapq as hq

class Map:
    def __init__(self, boundaries=None, obstacles=None):
        if boundaries is None:
            boundaries = [(0, 0), (0, 1), (1, 1), (1, 0)]
        self.map_region = Region(boundaries)
        self.obstacles = [Region(obstacle) for obstacle in obstacles]

    def shift(self, x_i, y_i, x_f, y_f):
        final_pos = (float("inf"), (x_f, y_f))
        for region in self.obstacles + [self.map_region]:
            collisions = region.intersect(x_i, y_i, x_f, y_f)
            if collisions:
                first_collision = collisions.heappop()
                final_pos = min(final_pos, first_collision)
        return final_pos[1]

    def contains(self, x, y):
        pass

    def plot_map(self, plot):
        self.map_region.plot_region(plot)
        for obstacle in self.obstacles:
            obstacle.plot_region(plot, facecolor='white')

