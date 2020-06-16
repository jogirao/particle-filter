import heapq as hq


class Region:
    def __init__(self, points):
        self.corners = points

    def intersect(self, x_i, y_i, x_f, y_f):
        # Computes the intersection points of the input line with the region borders, sorted in ascending order
        h = []
        for i in range(len(self.corners)):
            denominator = (x_i - x_f) * (self.corners[i - 1][1] - self.corners[i][1]) - (y_i - y_f) * (
                    self.corners[i - 1][0] - self.corners[i][0])
            # Non-parallel or coincident lines
            if denominator != 0:
                t = ((x_i - self.corners[i - 1][0]) * (self.corners[i - 1][1] - self.corners[i][1]) - (
                        y_i - self.corners[i - 1][1]) * (self.corners[i - 1][0] - self.corners[i][0])) / denominator
                u = ((x_i - self.corners[i - 1][0]) * (y_i - y_f) - (x_i - x_f) * (
                        y_i - self.corners[i - 1][1])) / denominator
                if not (t > 1 or t < 0 or u > 1 or u < 0):
                    # Lines intersect at point P
                    P = (x_i + t * (x_f - x_i), y_i + t * (y_f - y_i))
                    priority_point = (abs(P[0] - x_i) + abs(P[1] - y_i), P)
                    if priority_point not in h:
                        hq.heappush(h, priority_point)
        return h

    def plot_region(self, plot, facecolor='azure', edgecolor='lightblue'):
        edges = self.corners
        edges.append(edges[0])
        xs, ys = zip(*edges)
        plot.fill(xs, ys, facecolor=facecolor, edgecolor=edgecolor, linewidth=3)
