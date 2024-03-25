import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
class Visualizer:
    def __init__(self, particle_filter):
        self.particle_filter = particle_filter

    def start(self):
        # Do some logic, probably iterate through things
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        ax.axis([0, 1, 0, 1])
        # TODO THIS
        # m.plot_map(ax)
        # l, = ax.plot(0, 1, marker="o")
        # arrow = FancyArrow(xs[0], ys[0], orientation[0][0], orientation[0][1], color='r')
        # patch = ax.add_patch(arrow)
        #
        # def animate(i):
        #     l.set_data(xs[i], ys[i])
        #     ax.patches.pop()
        #     arrow = FancyArrow(xs[i], ys[i], orientation[i][0], orientation[i][1], color='r')
        #     patch = ax.add_patch(arrow)
        #
        # ani = animation.FuncAnimation(fig, animate, frames=len(movement_list) + 1, init_func=init, interval=1000)
        #
        # from IPython.display import HTML
        # HTML(ani.to_jshtml())
        # # self.particle_filter.move_agents(0, 0)