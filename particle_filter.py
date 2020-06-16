# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:09:29 2020

@author: joaom
"""

class particle_filter():
    
    import random as rd
    import matplotlib.pyplot as plt
    
    def __init__(self, nb_agents, map_nb=0):
        # Initialize environment
        self.map=get_map(map_nb)
        self.agents=get_agents(nb_agents, self.map)
        
    def make_map():
        # Create random map
        nb_points=4
        points=[]
        for p in range(nb_points):
            points.append((rd.uniform(0,1),rd.uniform(0,1)))
        return points
        
    def default_map(map_nb):
        # Get map from set of default maps
        Maps={1:[[(0,0),(0,1),(1,1),(1,0)]], 2:[[(0,0),(0,0.3),(0.2,0.3),(0.2,0.7),(0,0.7),(0,1),(0.3,1),(0.3,0.8),(0.7,0.8),(0.7,1),(1,1),(1,0.7),(0.8,0.7),(0.8,0.3),(1,0.3),(1,0),(0.7,0),(0.7,0.2),(0.3,0.2),(0.3,0)]], 3:[[(0,0),(0,0.3),(0.2,0.3),(0.2,0.7),(0,0.7),(0,1),(0.3,1),(0.3,0.8),(0.7,0.8),(0.7,1),(1,1),(1,0.7),(0.8,0.7),(0.8,0.3),(1,0.3),(1,0),(0.7,0),(0.7,0.2),(0.3,0.2),(0.3,0)],[(0.5,0.3),(0.5,0.6),(0.6,0.4),(0.59,0.29)]], 4:[[(0.2,0.2),(0.1,0.7),(0.5,0.9),(0.8,0.6),(0.7,0.3)]], 5:[[(0.2,0.2),(0.1,0.7),(0.5,0.9),(0.8,0.6),(0.7,0.3)],[(0.3,0.42),(0.3,0.58),(0.42,0.6),(0.5,0.6),(0.42,0.4)]], 6:[[(0.2,0.2),(0.1,0.7),(0.5,0.9),(0.8,0.6),(0.7,0.3)],[(0.3,0.35),(0.5,0.35),(0.5,0.45),(0.3,0.45)],[(0.3,0.7),(0.4,0.78),(0.42,0.65)],[(0.5,0.7),(0.7,0.6),(0.7,0.45),(0.6,0.46),(0.65,0.57)]]}
        try:
            return Maps[map_nb]
        except:
            print("Map number not available.")
            return []
    
    def points2series(Map):
        # Transforms coordinates to point series
        series_set=[]
        for area in Map:
            series=[[],[]]
            for point in area:
                series[0].append(point[0])
                series[1].append(point[1])
            series_set.append(series)
    
    def get_map(map_nb):
        # Initialize map
        if map_nb>0:
            return points2series(default_map(map_nb))
        else:
            return make_map()
        
    def plot_map(Map):
        # Plots map
        for area in Map:
            plt.pyplot(area[0],area[1],'k')
        plt.show()
        
        
        
    def get_agents(nb_agents):
        