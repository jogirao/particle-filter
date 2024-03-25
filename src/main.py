from src.structures.map import Map
from src.structures.agent import Agent
from src.particle_filter import ParticleFilter
from src.utils.config_utils import load_config
from src.visualizer import Visualizer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrow
import math


def main():
    # Load configuration
    config = load_config()
    # According to configuration, load model and entity
    particle_filter = ParticleFilter.init_from_config(config)
    if config['visualizer_state']:
        run_visualizer(particle_filter)
    else:
        # Logic without visualizer
        pass


def run_visualizer(particle_filter):
    # visualizer yes/no logic
    visualizer = Visualizer(particle_filter)
    # start it
    visualizer.start()


# def main():
#
#     # Initialize variables
#     borders=[[(0, 0), (0, 0.3), (0.2, 0.3), (0.2, 0.7), (0, 0.7), (0, 1), (0.3, 1), (0.3, 0.8), (0.7, 0.8),(0.7, 1), (1, 1), (1, 0.7), (0.8, 0.7), (0.8, 0.3), (1, 0.3), (1, 0), (0.7, 0), (0.7, 0.2),(0.3, 0.2), (0.3, 0)], [(0.5, 0.3), (0.5, 0.6), (0.6, 0.4), (0.59, 0.29)]]
#     entity_pos=(0.1, 0.15)
#     entity_orientation=math.pi/3
#     movement_list=((0.04, 0),(0.04, -math.pi/20),(0.04, -math.pi/20),(0.04, -math.pi/20),(0.03, -math.pi/20),(0.025, math.pi/20),(0.023, math.pi/20),(0.02, math.pi/20),(0.01, math.pi/20),(0,0),(0,-math.pi/100),(0,-math.pi/90),(0,-math.pi/85),(0,-math.pi/80),(0,-math.pi/80),(0.01,math.pi/100),(0.02,math.pi/100),(0.04,math.pi/100))
#
#     # Generate objects
#     m = Map(borders[0], borders[1:])
#     entity = Agent(entity_pos, entity_orientation)
#     state=ParticleFilter(nb_agents=30, nb_observations=3, map_nb=3)
#     agent_plots = [ax.plot(agent[0], agent[1], marker='o')[0] for agent in state.agents]

#arr = ax.arrow(*entity.coordinates,0.05*math.cos(entity.orientation),0.05*math.sin(entity.orientation),color='r')
# d=0.025
# xs, ys = [entity.coordinates[0]], [entity.coordinates[1]]
# orientation = [(d*math.cos(entity.orientation), d*math.sin(entity.orientation))]
# for movement in movement_list:
#     entity.move_agent(m, *movement)
#     xs.append(entity.coordinates[0])
#     ys.append(entity.coordinates[1])
#     orientation.append((d*math.cos(entity.orientation), d*math.sin(entity.orientation)))
#
# def update_pose(agent, move):
#     # Updates the entity's pose
#     agent.move_agent(m, *move)
#
    
"""
Matplot functions
"""

fig, ax = plt.subplots(1,1, figsize=(10, 10))
ax.axis([0,1,0,1])
m.plot_map(ax)
l, = ax.plot(0, 1,  marker="o")
arrow = FancyArrow(xs[0], ys[0], orientation[0][0], orientation[0][1], color='r')
patch = ax.add_patch(arrow)


def animate(i):
    l.set_data(xs[i], ys[i])
    ax.patches.pop()
    arrow = FancyArrow(xs[i], ys[i], orientation[i][0], orientation[i][1], color='r')
    patch = ax.add_patch(arrow)

ani = animation.FuncAnimation(fig, animate, frames=len(movement_list)+1, init_func=init, interval=1000)

from IPython.display import HTML
HTML(ani.to_jshtml())