import numpy as np
from scipy.signal import correlate2d
import matplotlib.pyplot as plt
from cell import Cell2D

from matplotlib import animation

class Diffusion:
    kernel = np.array([[0, 1, 0],
                   [1,-4, 1],
                   [0, 1, 0]])
    
    def __init__(self, rows, rate=0.1):
        self.rate = rate
        self.grid = np.zeros((rows, rows), np.float)
        self.image = None
        
    def add_cells(self, row, col, *strings):
        for i, string in enumerate(strings):
            self.grid[row+i, col:col+len(string)] = np.array([int(char) for char in string])
            
    def step(self):
        correlation = correlate2d(self.grid, self.kernel, mode='same')
        self.grid += self.rate * correlation
        
    def draw(self):
        options = dict(cmap='Reds', alpha=0.7, vmin=0, vmax=1,
                   interpolation='none', origin='upper')
        self.image = self.draw_grid(self.grid, **options)
        
    def draw_grid(self, grid, **options):
        x, y = grid.shape
        
        plt.axis([0, x, 0, y])
        plt.xticks([])
        plt.yticks([])
        
        return plt.imshow(grid, extent=[0, x, 0, y], **options)
        
    def animate(self):
        fig = plt.gcf()
        self.draw()
        
        a = animation.FuncAnimation(fig, self.animate_function, 
                                    init_func=self.init_func,
                                    frames=200,
                                    interval=0.1)
        return a
        
    def init_func(self):
        print('starting animation')
            
    def animate_function(self, i):
        if i > 0:
            self.step()
        try:
            self.image.set_array(self.grid)
        except:
            self.image.set_array(self.grid1)
            self.image.set_array(self.grid2)
        return (self.image,)
    
    def save_gif(self, name='my_gif'):
        writergif = animation.PillowWriter(fps=30)
        self.animate().save(name+'.gif', writer=writergif)
    
class Diffusion(Cell2D):
    kernel = np.array([[0, 1, 0],
                   [1,-4, 1],
                   [0, 1, 0]])
    
    def __init__(self, rows, rate=0.1):
        self.rate = rate
        self.grid = np.zeros((rows, rows), np.float)
        self.image = None
        
    def add_cells(self, row, col, *strings):
        for i, string in enumerate(strings):
            self.grid[row+i, col:col+len(string)] = np.array([int(char) for char in string])
            
    def step(self):
        correlation = correlate2d(self.grid, self.kernel, mode='same')
        self.grid += self.rate * correlation
    
    def draw(self):
        """Draws the cells."""
        self.image = self.draw_grid(self.grid, cmap='Reds')
        
        
if __name__ == '__main__':
    diffusion = Diffusion(10)
    diffusion.add_cells(3, 3, '111', '111', '111')
    diffusion.draw()
    #diffusion.animate(frames=20, interval=0.1)
    diffusion.save_gif()
