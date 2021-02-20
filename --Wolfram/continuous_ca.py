import numpy as np
import matplotlib.pyplot as plt
from math import floor

rows = 67
cols = rows


grid = np.zeros((rows, cols), dtype=float)

grid[0,rows//2] = 1

for i in range(1, rows):
    for j in range(1, cols-1):
        new_value = (grid[i-1, j-1] + grid[i-1, j] + grid[i-1, j+1])/3*-4.68 + .9
        
        if new_value > 1:
            new_value = new_value - floor(new_value)
        grid[i, j] = new_value
                
        

plt.imshow(grid, cmap='twilight')