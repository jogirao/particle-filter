import numpy as np
from math import pi, sqrt, cos, sin
from utils import process_radians
from map import Map


class Agent:
    def __init__(self, position, orientation=0, nb_observations=5):
        self.position = position
        self.orientation = orientation
        self.nb_observations = nb_observations
        self.radius = 0.5

    def get_observations(self, agent_map):
        # Compute agent observations
        angle_shift = pi / (2 * (self.nb_observations - 1))
        theta_0 = self.orientation - pi / 4
        observations = np.zeros(shape=(self.nb_observations,))
        for n in range(self.nb_observations):
            # Get distance to nearest wall
            obs_angle = ((theta_0 + n * angle_shift + pi) % (2 * pi)) - pi  # Normalized angle
            observations[n] = Map.get_observation(self.position, obs_angle)
        return observations

    def move(self, distance, angle):
        # Moves agent to new position in map (assumes quasi-linear movement)
        # Compute new position coordinates
        new_x = distance * cos(angle + self.orientation) + self.position[0]
        new_y = distance * sin(angle + self.orientation) + self.position[1]
        # Get new agent position considering possible collisions
        if Map.intersects(*self.position, new_x, new_y):
            new_x, new_y = Map.get_collision(self.position, (new_x, new_y))
            self.position = (new_x - self.radius * cos(angle + self.orientation),
                             new_y - self.radius * sin(angle + self.orientation))
            self.orientation = self.orientation + angle
