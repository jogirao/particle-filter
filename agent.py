import math
import numpy as np
from utils import process_radians


class Agent:
    def __init__(self, x, y, orientation=0, n_observations=3):
        self.coordinates = (x, y)
        self.orientation = orientation
        self.n_observations = n_observations

    def get_observations(self, agent_map):
        angle_shift = math.pi / (4 * (self.n_observations // 2))
        initial_observation = self.orientation - math.pi / 4
        distances = np.zeros(shape=(self.n_observations,))
        if not self.n_observations % 2:
            initial_observation += angle_shift / 2
        for n in range(self.n_observations):
            angle = process_radians(initial_observation + n * angle_shift)
            end_coordinates = agent_map.edge_intersect_by_pose(*self.coordinates, angle)
            x_f, y_f = agent_map.get_destination(*self.coordinates, *end_coordinates)
            distances[n] = math.sqrt((x_f - self.coordinates[0]) ** 2 + (y_f - self.coordinates[1]) ** 2)
        return distances

    def move_agent(self, agent_map, distance, angle):
        x = distance * math.cos(angle + self.orientation) + self.coordinates[0]
        y = distance * math.sin(angle + self.orientation) + self.coordinates[1]
        self.coordinates = agent_map.get_destination(*self.coordinates, x, y)
