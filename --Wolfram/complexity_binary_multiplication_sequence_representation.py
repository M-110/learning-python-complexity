"""This module saves visual representations of binary sequences.

The sequences are done through constant multiplication
"""
import matplotlib.pyplot as plt
from math import sqrt, log


def to_binary(num: int) -> str:
    """Convert int to string form of binary sequence"""
    return bin(num)[2:]

def binary_mult_image(multiplier: int = 2, length: int = 50):
    """Print a plot representing a simple sequence of binary numbers.
    
    Step corresponds to how many times to multiply"""
    grid = []
    n=1
    for i in range(1, length):
        grid.append([0]*(len(to_binary((multiplier**(length))))))
        for j, char in enumerate(to_binary(n)):
            #print(f'grid[{i-1}][{j}]', len(grid[i-1]))
            grid[i-1][j] = float(char)
        n = n*multiplier+1
        #print(grid)
            
    fig1 = plt.figure(figsize=(100,100))
    plt.pcolormesh(grid[::-1], cmap='Greens')
    plt.axis('off')
    plt.show()
    plt.draw()
    fig1.savefig(f'binary_image_mult_multiplier({multiplier})_length({length}).png', dpi=100)
    print(f'Saved as binary_image_mult_multiplier({multiplier})_length({length}).png')


# The first pattern using the multiplier 2 shows a solid simple triangle.
# But once you change the multiplier to 3, you can see the pattern becomes
# complex. 
# As you increase the multiple, you see about 4 pattern variations emerge.
base_size=5000
for i in range(2, 20):
    binary_mult_image(multiplier=i, length=base_size//i)
