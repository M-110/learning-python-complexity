from diffusion import Diffusion
import numpy as np
from scipy.signal import correlate2d
import matplotlib.pyplot as plt

from matplotlib import animation

class ReactionDiffusion(Diffusion):
    """Simulation of reaction diffusion using 2D cellular automata"""
    
    kernel = np.array([[.05, .2, .05],
                       [ .2, -1, .2],
                       [.05, .2, .05]])
    
    def __init__(self, rows, parameters, noise=0.1):
        self.parameters = parameters
        
        # Create first material as a solid square
        self.grid1 = np.ones((rows, rows), dtype=float)
        
        # Create second material as a bunch of noise
        self.grid2 = noise * np.random.random((rows, rows))
        
        self.add_island(self.grid2)
        
    def add_island(self, grid, height=0.1):
        x, y = grid.shape
        radius = min(x, y) // 20
        i = x//2
        j = y//2
        grid[i-radius:i+radius, j-radius:j+radius] += height
        
    def step(self):
        """Execute one step of diffusion"""
        a = self.grid1
        b = self.grid2
        ra, rb, f, k = self.parameters
        
        ca = correlate2d(a, self.kernel, mode='same', boundary='wrap')
        cb = correlate2d(b, self.kernel, mode='same', boundary='wrap')
        
        reaction = a * b**2
        
        self.grid1 += ra * ca - reaction + f * (1 - a)
        self.grid2 += rb * cb + reaction - (f + k) * b
        
    def draw(self):
        options = dict(interpolation='bicubic', vmin=None, vmax=None)
        self.image = self.draw_grid(self.grid1, cmap='Reds', **options)
        self.image += self.draw_grid(self.grid2, cmap='Blues', **options)
        
params1 = 0.5, 0.25, 0.035, 0.057   # pink spots and stripes
params2 = 0.5, 0.25, 0.055, 0.062   # coral
params3 = 0.5, 0.25, 0.039, 0.065   # blue spots

rd = ReactionDiffusion(rows=100, parameters=params1)
rd.draw()
rd.save_gif()