from json import loads
from math import floor, ceil, inf, sqrt, pi, tan


class Map:

    def __init__(self, map_choice="preset"):
        self.walls, self.wall_vertices_x, self.wall_vertices_y = [], [], []
        self.map_min_x, self.map_max_x, self.map_min_y, self.map_max_y = 0, 0, 0, 0
        self.build_map(map_choice)

    def build_map(self, map_choice):
        # Create map from collection of points stored in file
        # Get points from file
        with open("MapPointDict.txt", "r") as file:
            while not self.walls:
                string = file.readline()
                if string[: string.find(":")] == map_choice:
                    self.walls = loads(string[string.find(":") + 2 :])

        # Generate point series in x,x axis from group of points
        for wall in self.walls:
            wall_x, wall_y = [], []
            for point in wall:
                wall_x.append(point[0]), wall_y.append(point[1])
            self.wall_vertices_x.append(wall_x), self.wall_vertices_y.append(wall_y)

        min_x, max_x = min(min(x) for x in self.wall_vertices_x), max(
            max(x) for x in self.wall_vertices_x
        )
        min_y, max_y = min(min(y) for y in self.wall_vertices_y), max(
            max(y) for y in self.wall_vertices_y
        )
        self.map_min_x, self.map_max_x = min_x - floor(
            0.1 * (max_x - min_x)
        ), max_x + ceil(0.1 * (max_x - min_x))
        self.map_min_y, self.map_max_y = min_y - floor(
            0.1 * (max_y - min_y)
        ), max_y + ceil(0.1 * (max_y - min_y))

    def get_collision(self, line1_pt1: tuple, line1_pt2: tuple) -> tuple:
        # Get first collision between a line segment and the edges of a polygon
        coll_dist, coll_pt = inf, (0, 0)
        for wall in self.walls:
            for n in range(len(wall) - 1):
                line2_pt1, line2_pt2 = wall[n], wall[n + 1]
                # Check if both lines intersect
                if self.intersects(line1_pt1, line1_pt2, line2_pt1, line2_pt2):
                    # Get intersection point
                    new_coll_pt = self.get_collision_point(
                        line1_pt1, line1_pt2, line2_pt1, line2_pt2
                    )
                    # Update if distance to collision is smaller than current one
                    if (
                        dist := sqrt(
                            (new_coll_pt[1] - line1_pt1[1]) ** 2
                            + (new_coll_pt[0] - line1_pt1[0]) ** 2
                        )
                    ) < coll_dist:
                        coll_dist = dist
                        coll_pt = new_coll_pt
        return coll_pt

    def get_collision_point(
        self, line1_pt1: tuple, line1_pt2: tuple, line2_pt1: tuple, line2_pt2: tuple
    ) -> tuple:
        # Compute collision point
        if (line1_pt1[0] != line1_pt2[0]) & (line2_pt1[0] != line2_pt2[0]):
            # None of the lines is vertical
            m1, b1 = self.get_line_params(*line1_pt1, *line1_pt2)
            m2, b2 = self.get_line_params(*line2_pt1, *line2_pt2)
            if m1 == m2:
                # Collinear lines, get mean point
                x = (line1_pt1[0] + line1_pt2[0] + line2_pt1[0] + line2_pt2[0]) / 4
                y = (line1_pt1[1] + line1_pt2[1] + line2_pt1[1] + line2_pt2[1]) / 4
            else:
                # Crossing lines
                x = (b2 - b1) / (m1 - m2)
                y = m1 * x + b1
        elif (line1_pt1[0] == line1_pt2[0]) & (line2_pt1[0] == line2_pt2[0]):
            # Both lines vertical, return closest intersect with origin (assumed line1_pt2)
            x, y = line1_pt2
        elif line1_pt1[0] == line1_pt2[0]:
            # Line 1 vertical
            x = line1_pt1[0]
            m, b = self.get_line_params(*line2_pt1, *line2_pt2)
            y = m * x + b
        else:
            # Line 2 vertical
            x = line2_pt1[0]
            m, b = self.get_line_params(*line1_pt1, *line1_pt2)
            y = m * x + b
        return x, y

    @staticmethod
    def get_line_params(x1: int, y1: int, x2: int, y2: int) -> tuple:
        # Compute line parameters
        m = (y2 - y1) / (x2 - x1)  # Slope
        b = y1 - m * x1  # Y-intercept
        return m, b

    def get_observation(self, position: tuple, angle: float) -> tuple:
        # Compute observation (collision distance to nearest wall
        # Compute line parameters from point and angle
        m = tan(angle)  # Slope
        b = position[1] - m * position[0]  # Y-intercept
        # Compute end point coordinates
        if -(3 * pi) / 4 <= angle < -pi / 4:
            end_pt = ((self.map_min_y - b) / m, self.map_min_y)
        elif -pi / 4 <= angle < pi / 4:
            end_pt = (self.map_max_x, m * self.map_max_x + b)
        elif pi / 4 <= angle < (3 * pi) / 4:
            end_pt = ((self.map_max_y - b) / m, self.map_max_y)
        else:
            end_pt = (self.map_min_x, m * self.map_min_x + b)
        # Compute collision point with nearest wall
        return self.get_collision(position, end_pt)

    def intersects(self, p1: tuple, q1: tuple, p2: tuple, q2: tuple) -> bool:
        # Checks if 2 line segments ((p1,q1) and (p2,q2)) intersect
        o1, o2, o3, o4 = (
            self.orientation(p1, q1, p2),
            self.orientation(p1, q1, q2),
            self.orientation(p2, q2, p1),
            self.orientation(p2, q2, q1),
        )
        if o1 + o2 + o3 + o4 == 0:
            # Collinear line segments. Check if x-projections intersect
            max_x, min_x = max(p1[0], p2[0], q1[0], q2[0]), min(
                p1[0], p2[0], q1[0], q2[0]
            )
            if max_x - min_x <= abs(q1[0] - p1[0]) + abs(q2[0] - p2[0]):
                return True
        elif (o1 != o2) & (o3 != o4):
            return True
        return False

    def is_in_field(self, point: tuple, radius: float) -> bool:
        # Counts vertical/horizontal intersections with the walls
        left_hits, down_hits = 0, 0
        for wall_nb in range(len(self.wall_vertices_x)):
            # For each polygon
            wall_x_pts, wall_y_pts = (
                self.wall_vertices_x[wall_nb],
                self.wall_vertices_y[wall_nb],
            )
            for edge_nb in range(len(wall_x_pts) - 1):
                # For each wall, check if horizontal/vertical lines intersect
                x1, x2, y1, y2 = (
                    wall_x_pts[edge_nb],
                    wall_x_pts[edge_nb + 1],
                    wall_y_pts[edge_nb],
                    wall_y_pts[edge_nb + 1],
                )
                if self.intersects(
                    (point[0], self.map_min_y), point, (x1, y1), (x2, y2)
                ):
                    # Check if point is valid (collision point far enough away from agent)
                    coll_pt = self.get_collision_point(
                        (point[0], self.map_min_y), point, (x1, y1), (x2, y2)
                    )
                    if abs(point[1] - coll_pt[1]) < radius:
                        # Point too close to wall
                        return False
                    # Account for corners
                    if not ((point[0] == x1) & (point[0] == x1)):
                        if (point[0] == x1) | (point[0] == x2):
                            down_hits += 0.5 * (x2 - x1) / abs(x2 - x1)
                        else:
                            down_hits += 1
                if self.intersects(
                    (self.map_min_x, point[1]), point, (x1, y1), (x2, y2)
                ):
                    # Check if point is valid (collision point far enough away from agent)
                    coll_pt = self.get_collision_point(
                        point, (self.map_max_x, point[1]), (x1, y1), (x2, y2)
                    )
                    if abs(point[0] - coll_pt[0]) < radius:
                        # Point too close to wall
                        return False
                    # Account for corners
                    if not ((point[1] == y1) & (point[1] == y1)):
                        if (point[1] == y1) | (point[1] == y2):
                            left_hits += 0.5 * (y2 - y1) / abs(y2 - y1)
                        else:
                            left_hits += 1
        if (left_hits % 2 != 0) & (down_hits % 2 != 0):
            return True
        return False

    def line_intersects_map(self, line: list) -> bool:
        # Check if line collides with any map wall
        for polygon in self.walls:
            for edge_nb in range(len(polygon) - 1):
                if self.intersects(*line, polygon[edge_nb], polygon[edge_nb + 1]):
                    return True
        return False

    @staticmethod
    def orientation(p1, p2, p3) -> int:
        # Computes orientation given 3 points
        val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
        if val > 0:
            # Clockwise orientation
            return 1
        elif val < 0:
            # Counterclockwise orientation
            return 2
        # Collinear points
        return 0

    def plot(self, ax):
        # Plot map
        for nb in range(len(self.wall_vertices_x)):
            ax.plot(
                self.wall_vertices_x[nb],
                self.wall_vertices_y[nb],
                linewidth=2.0,
                color="k",
            )
            ax.set(
                xlim=(self.map_min_x, self.map_max_x),
                ylim=(self.map_min_y, self.map_max_y),
            )
