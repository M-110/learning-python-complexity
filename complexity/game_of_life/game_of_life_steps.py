"""A simple functional implementation of Conway's Game of Life."""

import numpy as np
from scipy.signal import correlate2d


def create_grid(x, y):
    return np.random.randint(2, size=(x, y), dtype=np.uint8)


grid = create_grid(10, 10)


def step_verbose(grid):
    """One step through the grid without correlate2d function"""
    # Create a new empty grid of the same shape as the input grid
    new_grid = np.zeros_like(grid)

    # Iterate through each cell in the grid.
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            # Get that cells current state.
            current_state = grid[i, j]

            # Get its 8 surrounding neighbors and itself.
            neighbors = grid[i - 1:i + 2, j - 1:j + 2]

            # Sum its neighbors and subtract itself.
            k = np.sum(neighbors) - current_state

            # If the cell is active.
            if current_state:
                # Remain active as long as it is surrounded by 2 or 3 other
                # active cells.
                if k == 2 or k == 3:
                    new_grid[i, j] = 1
            # If the cell is inactive
            else:
                # Reactivate cell if there are exactly 3 neighbors who are 
                # currently active
                if k == 3:
                    new_grid[i, j] = 1


def step(grid):
    """One step through the grid using correlate2d"""
    kernel = np.array([1, 1, 1],
                      [1, 10, 1],
                      [1, 1, 1])

    table = np.zeros(20, dtype=np.uint8)
    table[[3, 12, 13]] = 1

    # Get the cross correlation of the grid/pattern
    correlation = correlate2d(grid, kernel, mode='same')

    # Apply game of life rules
    life = (correlation == 3) | (correlation == 12) | (correlation == 13)

    #  Convert to int
    life = life.astype(np.uint8)
