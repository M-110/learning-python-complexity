"""This module saves visual representations of binary sequences.

The sequences are done by taking the previous value and adding the reverse
binary representation to get a new value.
"""
import matplotlib.pyplot as plt
from math import sqrt, log


def to_binary(num: int) -> str:
    """Convert int to string form of binary sequence"""
    return bin(num)[2:]

def reverse_digit(num: int) -> int:
    """Reverse the digits of an int."""
    return int(bin(num)[2:][::-1], 2)

def binary_image(num: int, initial_digit=2, width=100, step=1):
    """Print a plot representing a simple sequence of binary numbers.
    
    Step corresponds to how much to add"""
    grid = []
    digit = initial_digit
    for i in range(num//step):
        grid.append([0]*width)
        for j, char in enumerate(to_binary(digit)):
            grid[i][j] = float(char)
        digit = digit + reverse_digit(digit)
    fig1 = plt.figure(figsize=(100,100))
    plt.pcolormesh(grid[::-1], cmap='Greens')
    plt.axis('off')
    plt.show()
    plt.draw()
    fig1.savefig(f'initial_digit={initial_digit}.png', dpi=100)
   #fig1.savefig(f'binary_reversed_digit_addition_sequence_range({num})_initial_digit({initial_digit})_stepsize({step}).png', dpi=100)


for i in range(50):  
    binary_image(250, initial_digit=i, width=190, step=1)
for i in range(64, 512, 16):
    binary_image(250, initial_digit=i, width=190, step=1)
# When the initial digit is between 1 and 15, the only variations are in the
# first few rows. The patterns all quickly simplify to the same pattern.
#for i in range(1, 16): 
#    binary_image(200, initial_digit=i, width=110, step=1)

# When the initial digit is 16, you can see the pattern eventually terminates.
#binary_image(325, initial_digit=16, width=200, step=1)

# Changin the stepsize to 5 does not change the underlying pattern.
#binary_image(325*5, initial_digit=16, width=200, step=5)

# But using a diferent initial digit, 512, creates a different pattern which
# is complex and seemingly endless.
#binary_image(1125, initial_digit=512, width=750, step=1)

