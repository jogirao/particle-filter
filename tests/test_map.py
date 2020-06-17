from map import Map
from itertools import product


def test_map_empty():
    # Given a map with no arguments
    m = Map()
    # Then we have a map defined by the max regions, and no obstacles
    x_range, y_range = (m.x_min, m.x_max), (m.y_min, m.y_max)
    assert sorted(m.map_region.corners) == sorted([p for p in product(*[x_range, y_range])])
    assert not m.obstacles


def test_map_standard():
    # Given a map with defined arguments
    map_borders = [(0.2, 0.2), (0.1, 0.7), (0.5, 0.9), (0.8, 0.6), (0.7, 0.3)]
    boundaries = [[(0.3, 0.35), (0.5, 0.35), (0.5, 0.45), (0.3, 0.45)], [(0.3, 0.7), (0.4, 0.78), (0.42, 0.65)]]
    m = Map(map_borders, boundaries)
    # Then we obtained the expected map
    assert m.map_region.corners == map_borders
    assert all(obstacle.corners in boundaries for obstacle in m.obstacles)


def test_get_destination_no_collision():
    # Given the default map and a line that does not intersect the edges
    m = Map()
    point_i, point_f = (0.2, 0.5), (0.5, 0.5)
    # When we attempt to get the destination
    dest = m.get_destination(*point_i, *point_f)
    # Then we get the expected destination
    assert dest == point_f


def test_get_destination_simple_collision():
    # Given the default map and a line that intersects the edges
    m = Map()
    point_i, point_f = (0.2, 0.5), (1.5, 0.5)
    # When we attempt to get the destination
    dest = m.get_destination(*point_i, *point_f)
    # Then we get the collision
    assert dest == (1.0, 0.5)


def test_get_destination_vortex():
    # Given the default map and a line that intersects the vortex
    m = Map()
    point_i, point_f = (0.5, 0.5), (1.5, 1.5)
    # When we attempt to get the destination
    dest = m.get_destination(*point_i, *point_f)
    # Then we get the collision
    assert dest == (1.0, 1.0)


def test_get_destination_on_edge():
    # Given the default map and a line that ends on an edge
    m = Map()
    point_i, point_f = (0.5, 0.5), (0.5, 1.0)
    # When we attempt to get the destination
    dest = m.get_destination(*point_i, *point_f)
    # Then we get the collision
    assert dest == point_f

#     def get_destination(self, x_i, y_i, x_f, y_f):
#         final_pos = (float("inf"), (x_f, y_f))
#         for region in self.obstacles + [self.map_region]:
#             collisions = region.intersect(x_i, y_i, x_f, y_f)
#             if collisions:
#                 first_collision = hq.heappop(collisions)
#                 final_pos = min(final_pos, first_collision)
#         return final_pos[1]
#
#     def contains(self, x, y):
#         n_intersections = sum(len(region.intersect(x, y, self.x_min, y)) for region in self.obstacles + [self.map_region])
#         return n_intersections % 2
#
#     def edge_intersect_by_pose(self, x, y, angle):
#         quarter_pi = math.pi / 4
#         if quarter_pi < angle <= 3 * quarter_pi:
#             return round((self.y_max - y) / math.tan(angle) + x, 8), self.y_max
#         elif -3 * quarter_pi < angle <= - quarter_pi:
#             return round((self.y_min - y) / math.tan(angle) + x, 8), self.y_min
#         elif -quarter_pi < angle <= quarter_pi:
#             return self.x_max, round((self.x_max - x) * math.tan(angle) + y, 8)
#         else:
#             return self.x_min, round((self.x_min - x) * math.tan(angle) + y, 8)
#
#     def plot_map(self, plot):
#         self.map_region.plot_region(plot)
#         for obstacle in self.obstacles:
#             obstacle.plot_region(plot, facecolor='white')
