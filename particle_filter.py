import random as rd
import matplotlib.pyplot as plt
from map import Map

class ParticleFilter:

    def __init__(self, nb_agents=5, map_nb=0):
        # Initialize environment
        self.map = self.get_map(map_nb)
#        self.agents = self.get_agents(nb_agents, self.map)

    def make_map(self):
        # Create random map
        """
        In progress
        """
        return []

    def default_map(self, map_nb):
        # Get map from set of default maps
        maps = {1: [[(0, 0), (0, 1), (1, 1), (1, 0)]], 2: [
            [(0, 0), (0, 0.3), (0.2, 0.3), (0.2, 0.7), (0, 0.7), (0, 1), (0.3, 1), (0.3, 0.8), (0.7, 0.8), (0.7, 1),
             (1, 1), (1, 0.7), (0.8, 0.7), (0.8, 0.3), (1, 0.3), (1, 0), (0.7, 0), (0.7, 0.2), (0.3, 0.2), (0.3, 0)]],
                3: [[(0, 0), (0, 0.3), (0.2, 0.3), (0.2, 0.7), (0, 0.7), (0, 1), (0.3, 1), (0.3, 0.8), (0.7, 0.8),
                     (0.7, 1), (1, 1), (1, 0.7), (0.8, 0.7), (0.8, 0.3), (1, 0.3), (1, 0), (0.7, 0), (0.7, 0.2),
                     (0.3, 0.2), (0.3, 0)], [(0.5, 0.3), (0.5, 0.6), (0.6, 0.4), (0.59, 0.29)]],
                4: [[(0.2, 0.2), (0.1, 0.7), (0.5, 0.9), (0.8, 0.6), (0.7, 0.3)]],
                5: [[(0.2, 0.2), (0.1, 0.7), (0.5, 0.9), (0.8, 0.6), (0.7, 0.3)],
                    [(0.3, 0.42), (0.3, 0.58), (0.42, 0.6), (0.5, 0.6), (0.42, 0.4)]],
                6: [[(0.2, 0.2), (0.1, 0.7), (0.5, 0.9), (0.8, 0.6), (0.7, 0.3)],
                    [(0.3, 0.35), (0.5, 0.35), (0.5, 0.45), (0.3, 0.45)], [(0.3, 0.7), (0.4, 0.78), (0.42, 0.65)],
                    [(0.5, 0.7), (0.7, 0.6), (0.7, 0.45), (0.6, 0.46), (0.65, 0.57)]]}
        try:
            return maps[map_nb]
        except:
            print("Map number not available.")
            return []

    def get_map(self, map_nb):
        # Initialize map
        if map_nb > 0:
            areas=self.default_map(map_nb)
        else:
            areas=self.make_map()
        if areas:
            if len(areas)>1:
                return Map(areas[0], areas[1:])
            else:
                return Map(areas[0])
        else:
            return Map()

    def plot_environment(self):
        # Plots map
        plt.figure(figsize=(20, 20))
        self.map.plot_map(plt)
        for agent in self.agents:
            plt.plot(agent.coordinates[0], agent.coordinates[1], marker="o", color='k')
        plt.show()

#    def get_agents(self, nb_agents):
#        return
