import math
import random as rd
from src.structures.agent import Agent
from src.utils.process_input import load_map, load_entity
from math import pi


class ParticleFilter:

    def __init__(self, background, agent, movements=None, nb_estimates=10, nb_observations=3):
        self.background = background
        self.agent = agent
        self.movements = movements
        self.estimates = []
        self.generate_initial_estimates(nb_estimates, nb_observations)

    # TODO review & refactor config files and methods
    @classmethod
    def init_from_config(cls, config):
        background = load_map(config['map'])
        agent, movements = load_entity(config['agent'])
        cls(background, agent, movements, config['nb_estimates'], config['nb_observations'])

    def generate_initial_estimates(self, nb_estimates: int, nb_observations: int) -> None:
        # Initial agent configuration
        min_x, max_x = self.background.map_min_x, self.background.map_max_x
        min_y, max_y = self.background.map_min_y, self.background.map_max_y
        while len(self.estimates) < nb_estimates:
            # Generate agent pose
            position = (rd.uniform(min_x, max_x), rd.uniform(min_y, max_y))
            while not self.background.is_in_field(position, self.agent.radius):
                position = (rd.uniform(min_x, max_x), rd.uniform(min_y, max_y))
            orientation = rd.uniform(-math.pi, math.pi)
            self.estimates.append(Agent(position, orientation, nb_observations, 'b'))

    def generate_new_estimates(self) -> None:
        # Generate new estimates
        roulette = self.generate_roulette()
        # Computes the position of the next iteration of agents
        new_estimates = []
        for i in range(len(self.estimates)):
            estimate_nb = self.spin_roulette(roulette)
            new_estimates.append(self.create_new_agent(estimate_nb))
        self.estimates = new_estimates

    def generate_roulette(self) -> list:
        # Generates a roulette-like probability function based on the likelihood of the estimates being the truth
        roulette = []
        truth = self.agent.get_observations(self.background, 'noisy')
        for estimate in self.estimates:
            observations = estimate.get_observations(self.background)
            roulette.append(self.compute_fit(truth, observations))
        # Normalize roulette
        roulette_sum = sum(roulette)
        slot_sum = 0
        for slot_nb in range(len(roulette)):
            slot_sum += (roulette[slot_nb] / roulette_sum)
            roulette[slot_nb] = slot_sum
        # Ensure that the probability function ends with value 1
        roulette[-1] = 1
        return roulette

    @staticmethod
    def compute_fit(truth: list, estimate: list) -> float:
        # Computes the estimate's fit
        error = 0
        for i in range(len(truth)):
            error += (truth[i] - estimate[i]) ** 2
        return len(truth) / error

    @staticmethod
    def spin_roulette(roulette: list) -> int:
        # Generates an integer based on a roulette like probability list
        slot, value = 0, rd.uniform(0, 1)
        while value > roulette[slot]:
            slot += 1
        return slot

    def create_new_agent(self, estimate_nb: int) -> Agent:
        # Generates a new set of agents from the selected ones
        position = self.estimates[estimate_nb].position
        orientation = self.estimates[estimate_nb].orientation
        nb_observations = self.estimates[estimate_nb].nb_observations
        radius = self.estimates[estimate_nb].radius
        # Add uncertainty
        new_position = (rd.gauss(position[0], radius), rd.gauss(position[1], radius))
        while not self.background.is_in_field(new_position, radius):
            new_position = (rd.gauss(position[0], radius), rd.gauss(position[1], radius))
        new_orientation = (orientation + pi) % (2 * pi) - pi
        new_agent = Agent(new_position, new_orientation, nb_observations, 'b')
        return new_agent
