"""This module saves visual representations of binary sequences.

The sequences are done through constant addition.
"""
import matplotlib.pyplot as plt
from math import sqrt, log
import os
from random import randint


class BinaryGrapher:
    def __init__(self, rows: int, starting_value: int = 1, step_size: int = 1):
        self.rows = rows
        self.starting_value = starting_value
        self.step_size = step_size
        self.grid = []
    
    @staticmethod
    def int_to_binary_string(num: int) -> str:
        """Convert int to its binary equivilent and return as string"""
        return bin(num)[2:]
    
    def generate_grid(self):
        self.grid = []
        n = self.starting_value
        for i in range(0, self.rows, self.step_size):
            self.grid.append([float(char) for char in self.int_to_binary_string(n)])
            n = self.step_function(n, i) 
        self.fill_grid()
            
    def fill_grid(self):
        width = len(self.grid[-1])
        for i in range(len(self.grid)):
            padding = width - len(self.grid[i])
            self.grid[i] += [0] * padding
    
    def draw_graph(self, cmap='Greens', figsize=(50,100)):
        if self.grid == []:
            self.generate_grid()
            
        self.fig = plt.figure(figsize=figsize)
        plt.pcolormesh(self.grid[::-1], cmap=cmap)
        
    def save_image(self, filename, folder='', cmap='Greens', figsize=(50,100),
                   dpi=100):
        self.draw_graph(cmap=cmap, figsize=figsize)
        self.fig.savefig(os.path.join(folder, filename + '.png'), dpi=dpi)
        
        
    def step_function(self, n: int, i: int):
        return n * 2 + i
    
        raise NotImplementedError('A step_function must be implimented in '
                                  f'{self.__class__.__name__!r} class.')
    
if __name__ == "__main__": 
    grapher = BinaryGrapher(34, step_size=1)
    grapher.draw_graph()

#for i in range(1, 10):
#    grapher = BinaryGrapher(1000*i, step_size=i)
#    grapher.save_image(f'step_size_{i}', 'test', cmap='Greens')