from math import pi, cos, sin
from matplotlib.patches import FancyArrow


class Agent:
    def __init__(self, position, orientation=0, nb_observations=5, color="g"):
        self.position = position
        self.orientation = orientation
        self.nb_observations = nb_observations
        self.radius = 4
        self.color = color

    def get_observations(self, map, obs_nature='clean'):
        # Compute agent observations
        angle_shift = pi / (2 * (self.nb_observations - 1))
        theta_0 = self.orientation - pi / 4
        observations = []
        for n in range(self.nb_observations):
            # Get distance to nearest wall
            obs_angle = (
                (theta_0 + n * angle_shift + pi) % (2 * pi)
            ) - pi  # Normalized angle
            observations.append(map.get_observation(self.position, obs_angle, obs_nature))
        return observations

    def move(self, map, distance: float, angle: float):
        # Moves agent to new position in map (assumes quasi-linear movement)
        # Compute new position coordinates
        new_x = distance * cos(angle + self.orientation) + self.position[0]
        new_y = distance * sin(angle + self.orientation) + self.position[1]
        # Get new agent position considering possible collisions
        if map.line_intersects_map([self.position, (new_x, new_y)]):
            new_x, new_y = map.get_collision(self.position, (new_x, new_y))
        self.position = (
            new_x - self.radius * cos(angle + self.orientation),
            new_y - self.radius * sin(angle + self.orientation),
        )
        self.orientation = self.orientation + angle

    def plot(self, ax):
        # Plot map
        ax.plot(self.position[0], self.position[1], marker="o", color=self.color, ms=4)
        ax.add_patch(
            FancyArrow(
                self.position[0],
                self.position[1],
                4 * cos(self.orientation),
                4 * sin(self.orientation),
                color=self.color,
            )
        )
