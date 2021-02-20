import numpy as np
import matplotlib.pyplot as plt
from time import sleep

from matplotlib import animation


class Cell2D:
    """Base class for 2D cellular automata."""
    
    def __init__(self, rows, cols=None):
        if cols is None:
            cols = rows
        self.grid = np.zeros((rows, cols), np.uint8)
        
    def add_cells(self, row, col, *strings):
        for i, string in enumerate(strings):
            self.grid[row+i, col:col+len(string)] = np.array([int(c) for c in string])
            
    def loop(self, count=1):
        for i in range(count):
            self.step()
            
    def step():
        pass
    
    def draw(self, **options):
        self.image = self.draw_grid(self.grid, **options)
        
    def draw_grid(self, grid, **options_):
        x, y = grid.shape
        options = dict(cmap='Greens', alpha=.7, vmin=0, vmax=1,
                            interpolation='none', origin='upper',
                            extent = [0, x, 0, y])
        options.update(options_)
        
        plt.axis([0, x, 0, y])
        plt.xticks([])
        plt.yticks([])
        
        #return plt.imshow(grid, cmap='YlOrRd', alpha=.7, vmin=0, vmax=5, interpolation='none', origin='upper',extent = [0, x, 0, y])
        
        return plt.imshow(grid, cmap='Blues', alpha=.3, vmax=4)
    
    def animate(self, frames, interval=None, step=None):
        if step is None:
            step = self.step
            
        plt.figure()
        try:
            for i in range(frames-1):
                self.draw()
                plt.show()
                if interval:
                    sleep(interval)
                step()
            self.draw()
            plt.show()
        except KeyboardInterrupt:
            pass
        
    def save_gif(self, filename='my_gif', frames=200, interval=0.1, fps=30):
        writergif = animation.PillowWriter(fps=fps)
        self.animate_gif(frames, interval).save(filename+'.gif', 
                                                writer=writergif)
        
    def animate_gif(self,frames, interval):
        fig = plt.gcf()
        self.draw()
        
        a = animation.FuncAnimation(fig, self.animate_function,
                                   init_func=self.init_func,
                                   frames=frames, interval=interval)
        return a
    
        
    def init_func(self):
        print('starting animation')
            
    def animate_function(self, i):
        if i > 0:
            self.step()
            
        self.image.set_array(self.grid)
        
        return (self.image,)
    