"""This simulates percolation which is the process of fluid flowing through
semi-porous materials such as water through paper.

Multiple gifs are saved with various parameters.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate2d

from complexity.game_of_life.cell_2d import Cell2D


class Percolation(Cell2D):
    """CA Simulation of percolation."""

    kernel = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]])
    
    def __init__(self, n: int, q: float = 0.5):
        self.q = q
        self.array = np.random.choice([1, 0], (n, n), p=[q, 1-q])
        
        # Initial conditions
        self.array[0] = 5
        
    def step(self):
        """Simulation of one step."""
        a = self.array
        c = correlate2d(a, self.kernel, mode='same')
        self.array[(a == 1) & (c >= 5)] = 5 
        
    @property
    def num_wet(self) -> int:
        """Returns total number of wet cells."""
        return int(np.sum(self.array == 5))
    
    @property
    def is_bottom_row_wet(self) -> int:
        """Returns True if there are wet cells in the bottom row."""
        return int(np.sum(self.array[-1] == 5))
    
    def draw(self):
        """Draw cells."""
        x, y = self.array.shape
        plt.axis([0, y, 0, x])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(self.array, cmap='cool', vmax=8)
        self.image = plt.gci()


if __name__ == '__main__':
    for i in [.55, .57, .6, .63, .65, .7, .75, .8]:
        perc = Percolation(200, i)
        perc.save_gif(f'percolation_q_{i}', frames=500, fps=30)
