import numpy as np
from scipy.signal import correlate2d
from cell import Cell2D


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
    diffusion.animate(frames=20, interval=0.1)
    diffusion.save_gif()
