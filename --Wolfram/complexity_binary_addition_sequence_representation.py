"""This module saves visual representations of binary sequences.

The sequences are done through constant addition.
"""
import matplotlib.pyplot as plt
from math import sqrt, log


def to_binary(num: int) -> str:
    """Convert int to string form of binary sequence"""
    return bin(num)[2:]

def binary_image(num: int, step=1):
    """Print a plot representing a simple sequence of binary numbers.
    
    Step corresponds to how much to add"""
    grid = []
    for i in range(num//step):
        grid.append([0]*int(log(num, 2)+1))
        for j, char in enumerate(to_binary(i*step)):
            grid[i][j] = float(char)
    fig1 = plt.figure(figsize=(25,100))
    plt.pcolormesh(grid[::-1], cmap='Greens')
    plt.axis('off')
    plt.show()
    plt.draw()
    fig1.savefig(f'binary_image_addition_range({num})_stepsize({step}).png', dpi=100)


# The visual pattern remains the same regardless of the stepsize you use.
# Evenly spaced sequences in binary seem to have a universal visual pattern.
binary_image(500, step=1)
binary_image(500*3, step=3)
binary_image(500*13, step=13)
binary_image(500*25, step=25)
binary_image(500*87, step=87)