"""Simulation of diffusion using the Cell2D parent class.

The example creates a smaller square as the initial conditions as well saves
the result as a gif which shows the red square diffuse until it has disappeared.
"""
import numpy as np
from scipy.signal import correlate2d

from complexity.game_of_life.cell_2d import Cell2D


class Diffusion(Cell2D):
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])

    def __init__(self, rows, rate=0.1):
        super().__init__(rows)
        self.array = np.zeros((rows, rows), np.float)
        self.rate = rate
        
    def step(self):
        correlation = correlate2d(self.array, self.kernel, mode='same')
        self.array += self.rate * correlation


if __name__ == '__main__':
    diffusion = Diffusion(15)
    diffusion.set_plot_options(cmap='Reds', vmax=1)
    diffusion.add_cells(7, 7, ['111', '111', '111'])
    diffusion.save_gif(filename='simple_diffusion', frames=200, interval=0.1, fps=20)
