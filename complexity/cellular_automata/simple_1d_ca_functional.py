import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
from random import randint


def generate_array(rows, cols):
    """Create a 2d array"""
    array = np.zeros((rows, cols), dtype=np.uint8)
    return array


def step(array, i):
    """Generate row i based on the above row"""
    rows, cols = array.shape

    # Select the previous row for calculating the next row
    previous_row = array[i - 1]

    # Iterate through all the columns
    for j in range(1, cols):
        # Get the 3 neighbors above current cell
        neighbors = previous_row[j - 1:j + 2]

        # Set the new cell to be the sum of it's above neighbors and
        # use the modulus operator to restrict to 0 or 1
        array[i, j] = sum(neighbors) % 2


def alt_step(array, i):
    """Generate row i based on the above row. Alternative method."""
    rows, cols = array.shape

    # Select the previous row for calculating the next row
    previous_row = array[i - 1]

    # Iterate through all the columns
    for j in range(1, cols):
        # Get the 5 neighbors above current cell
        neighbors = previous_row[j - 2:j + 3]

        # Set the new cell to be the sum of it's above neighbors and
        # use the modulus operator to restrict to 0 or 1
        array[i, j] = sum(neighbors) % 2


def fast_step(array, i, window=[1, 1, 1]):
    """A more efficient step function that use 2d correlation."""
    previous_row = array[i - 1]

    # use the np.correlate function to speed up the step calculations
    correlation = np.correlate(previous_row, window, mode='same')
    print(correlation % 2)
    array[i] = correlation % 2


def step_over_all_rows(array, step_function):
    # Iterate through all rows in the array
    for i in range(1, array.shape[0]):
        step_function(array, i)
    plt.imshow(array)
    plt.show()


if __name__ == "__main__":
    rows = 50
    cols = 100

    # Create an array
    array = generate_array(rows, cols)

    # Set initial conditions
    array[0, 50] = 1

    # Step through all rows of array and print plot

    step_over_all_rows(array, fast_step)
