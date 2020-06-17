import matplotlib.pyplot as plt
import math
import numpy as np
import random as rd
from map import Map
from agent import Agent


class ParticleFilter:

    def __init__(self, nb_agents=5, nb_observations=3, map_nb=0):
        # Initialize environment
        self.map = self.get_map(map_nb)
        self.get_agents(nb_agents, nb_observations)
        
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
        # Plots world state
        plt.figure(figsize=(20, 20))
        self.map.plot_map(plt)
        for agent in self.agents:
            plt.plot(agent.coordinates[0], agent.coordinates[1], marker="o", color='k')
        plt.show()

    def get_agents(self, nb_agents, nb_observations):
        # Initial agent configuration
        self.agents=[]
        for i in range(nb_agents):
            # Attribute initialization
            coords=(rd.uniform(0,1),rd.uniform(0,1))
            while not self.map.contains(*coords):
                coords=(rd.uniform(0,1),rd.uniform(0,1))
            orientation=rd.uniform(-math.pi, math.pi)
            # Create agent
            self.agents.append(Agent(coords, orientation))
            
    def create_next_iteration_agents(self, observation):
        # Computes the position of the agents in the next iteration
        base_agents=self.select_agents(self.fit_agent_universe(observation))
        self.new_agents(base_agents)
        
    def select_agents(self, fit_list):
        # Select list of agents that are going to be used as a base for the next iteration
        s=0
        normalized_summed_list=np.array([])
        for i in fit_list:
            s+=i
            normalized_summed_list.append(s)
        normalized_summed_list/=normalized_summed_list[-1]
        return self.roulette(len(normalized_summed_list), normalized_summed_list)
    
    def roulette(nb_plays, probability_list):
        # Computes the final position based on the probability list
        result=[]
        for i in range(nb_plays):
            num=rd.uniform(0,1)
            index=0
            while num>probability_list[index]:
                index+=1
            result.append(index)
        return result
    
    def new_agents(self, agent_selection, sigma=1/20):
        # Generates a new set of agents from the selected ones
        index=0
        for i in agent_selection:
            base=self.agents[i].coordinates
            new_pos=(rd.gauss(base[0], sigma), rd.gauss(base[1], sigma))
            while not self.map.contains(*new_pos):
                new_pos=(rd.gauss(base[0], sigma), rd.gauss(base[1], sigma))
            self.agents[index]=new_pos
            index+=1
        
    def fit_agent_universe(self, observation):
        # Returns the fit of each agent according to the entity's observation.
        fit=[]
        for agent in self.agent:
            fit.append(1/((self.mse(agent.get_observations, observation)**2)+1))
        return fit
    
    def mse(goal, data):
        # Mean squared error of the data
        return ((goal-data)**2)/len(goal)
    
    def move_agents(self, movement, error=(0, 0)):
        # Moves agents according to input movement
        for agent in self.agents:
            agent.move_agent(self.map, movement[0]+error[0], movement[1]+error[1])
            