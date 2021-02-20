import numpy as np
import matplotlib.pyplot as plt
from random import randint

from matplotlib import animation
from scipy.signal import convolve2d, correlate2d

class Life:
    """Conway's Game of Life implimentation.
    
    Args:
        rows: number of rows in the grid
        cols: number of columns in the grid
    """
    
    def __init__(self, rows, cols=None):
        # Default to square grid if cols not provided
        if cols is None:
            cols = rows
            
        # Initialize the empty grid
        self.grid = np.zeros((rows, cols), np.uint8)
        
        self.kernel = np.array([[1, 1, 1],
                               [1, 10, 1],
                               [1, 1, 1]])
        # Create an empty array of length 20      
        self.table = np.zeros(20, dtype=np.uint8)
        
        # Set the 3rd, 12th and 13th value to 1
        self.table[[3, 12, 13]] = 1
        self.step_count = 0
        self.image = None
        self.prev_grid = np.zeros((rows, cols), np.uint8)
        
        self.change_sequence =[]
        
        
    def step(self):
        """Execute 1 step using the game's rules"""
        self.step_count += 1
        correlation = correlate2d(self.grid, self.kernel, mode='same')
        
        
        prev_prev_grid = self.prev_grid
        self.prev_grid = self.grid
        self.grid = self.table[correlation]
        
        changed_cells = np.sum(self.grid != self.prev_grid)
        #print(changed_cells)
        self.change_sequence.append(changed_cells)
        if (self.grid == prev_prev_grid).all():
            #print(f'Stabalized at {self.step_count}')
            return False
        return True
        
    def make_life(self, row, col, *strings):
        """Create grid squares beginning at position (row, col) using strings"""
        for i, string in enumerate(strings):
            self.grid[row + i, col:(col + len(string))] = np.array(
                [int(char) for char in string])
            
    def draw(self):
        """Draw the grid"""
        g = self.grid.copy()
        cmap = plt.get_cmap('Greens')
        options = dict(interpolation='nearest', alpha=0.8, vmin=0, vmax=1, origin='upper')
        
        # Get width/height of grid for plotting
        x, y = g.shape
        plt.axis([0, x, 0, y])
        plt.xticks([])
        plt.yticks([])
        
        self.image = plt.imshow(g, cmap, **options)
        
    def run_until_stable(self):
        stable = True
        step_count = 0
        while stable:
            step_count += 1
            stable = self.step()
            if step_count > 10000:
                break
        return step_count
    
    def flip_random_cell(self):
        random_x = randint(0, self.grid.shape[0]-1)
        random_y = randint(0, self.grid.shape[0]-1)
        self.grid[random_x, random_y] = abs(self.grid[random_x, random_y] - 1)
        
    def run_n_iterations(self, n):
        steps = []
        for i in range(n):
            step_count = self.run_until_stable()
            self.flip_random_cell()
            steps.append(step_count)
        return steps, self.change_sequence
            
        
        
    def animate(self):
        fig = plt.gcf()
        self.draw()
        
        a = animation.FuncAnimation(fig, self.animate_function, 
                                    init_func=self.init_func,
                                    frames=1000,
                                    interval=200)
        return a
        
    def init_func(self):
        print('starting animation')
            
    def animate_function(self, i):
        if i > 0:
            stable = self.step()
        
        self.image.set_array(self.grid)
        return (self.image,)
        
        
        
if __name__ == "__main__":
    size = 100
    life = Life(size)
    
    for i in range(size):
        for j in range(size):
            life.make_life(i,j,str(randint(0,1)))
    life.run_n_iterations(500)