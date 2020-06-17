from region import Region
import math
import heapq as hq


class Map:
    x_min, x_max, y_min, y_max = 0, 1, 0, 1

    def __init__(self, boundaries=None, obstacles=None):
        if boundaries is None:
            boundaries = [(0, 0), (0, 1), (1, 1), (1, 0)]
        if obstacles is None:
            obstacles = []
        self.map_region = Region(boundaries)
        self.obstacles = [Region(obstacle) for obstacle in obstacles]

    def get_destination(self, x_i, y_i, x_f, y_f):
        final_pos = (float("inf"), (x_f, y_f))
        for region in self.obstacles + [self.map_region]:
            collisions = region.intersect(x_i, y_i, x_f, y_f)
            if collisions:
                first_collision = hq.heappop(collisions)
                final_pos = min(final_pos, first_collision)
        return final_pos[1]

    def contains(self, x, y):
        return False

    def edge_intersect_by_pose(self, x, y, angle):
        quarter_pi = math.pi / 4
        if quarter_pi < angle <= 3 * quarter_pi:
            return round((self.y_max - y) / math.tan(angle) + x, 8), self.y_max
        elif -3 * quarter_pi < angle <= - quarter_pi:
            return round((self.y_min - y) / math.tan(angle) + x, 8), self.y_min
        elif -quarter_pi < angle <= quarter_pi:
            return self.x_max, round((self.x_max - x) * math.tan(angle) + y, 8)
        else:
            return self.x_min, round((self.x_min - x) * math.tan(angle) + y, 8)

    def plot_map(self, plot):
        self.map_region.plot_region(plot)
        for obstacle in self.obstacles:
            obstacle.plot_region(plot, facecolor='white')
