from sandpile import SandPile
import numpy as np
import matplotlib.pyplot as plt

class SingleSource(SandPile):
    """A sand pile that starts with a single cell"""
    def __init__(self, rows, cols=None, level=9):
        if cols is None:
            cols = rows
        self.grid = np.zeros((rows, cols), dtype=np.int32) * level
        self.grid[rows//2][cols//2] = 50000
        self.toppled_sequence = []
    
if __name__ == "__main__":
    single_source = SingleSource(150, level=5)
    single_source.draw_after_n_iterations(1)