from src.structures.region import Region


def test_init_region():
    # Given a list of points
    corners = [(0, 0), (0, 1), (1, 0), (1, 1)]
    # When we initialise a region
    region = Region(corners)
    # Then the region has the expected corners
    assert region.corners == corners


def test_intersect_success():
    # Given a region
    region = Region([(0, 0), (0, 0.5), (0.5, 0.5), (0.5, 0)])
    # When we check for intersections with a segment that goes through it
    point_i, point_f = (0.2, 0.7), (0.7, 0.2)
    collisions = region.intersect(*point_i, *point_f)
    # Then we get two collisions, with a measure of proximity
    expected_collisions = [(0.4, (0.4, 0.5)), (0.6, (0.5, 0.4))]
    assert len(collisions) == 2
    assert all(collision == expected_collisions[i] for i, collision in enumerate(collisions))


def test_intersect_empty():
    # Given a region
    region = Region([(0, 0), (0, 1), (1, 1), (1, 0)])
    # When we check for intersections with a segment that does not go through it
    point_i, point_f = (0.2, 0.2), (0.7, 0.2)
    collisions = region.intersect(*point_i, *point_f)
    # Then we get no collisions
    assert not len(collisions)

def test_intersect_vortex():
    # Given a region
    vortex_to_intersect = (0.5, 0.5)
    region = Region([(0, 0), (0, 0.5), vortex_to_intersect, (0.5, 0)])
    # When we check for intersections with a segment that goes through the vortex
    point_i, point_f = (0.25, 0.75), (0.75, 0.25)
    collisions = region.intersect(*point_i, *point_f)
    # Then we get no duplicates and we get one intersection
    assert len(collisions) == 1
    assert collisions[0][1] == vortex_to_intersect

#
#     def plot_region(self, plot, facecolor='azure', edgecolor='lightblue'):
#         edges = self.corners
#         edges.append(edges[0])
#         xs, ys = zip(*edges)
#         plot.fill(xs, ys, facecolor=facecolor, edgecolor=edgecolor, linewidth=3)
