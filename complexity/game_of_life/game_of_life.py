"""An implementation of Conway's game of life using the Cell2D parent class.

The initial state used in the example below is a 'glider gun' which is an endless
looping pattern that keeps producing moving objects that look like gliders.
"""

import numpy as np
from scipy.signal import correlate2d

from complexity.game_of_life.cell_2d import Cell2D


class Life(Cell2D):
    """Conway's Game of Life implementation.

    Args:
        rows: number of rows in the grid
        cols: number of columns in the grid
    """

    def __init__(self, rows, cols=None):
        # Default to square grid if cols not provided
        super().__init__(rows, cols)

        self.kernel = np.array([[1, 1, 1],
                                [1, 10, 1],
                                [1, 1, 1]])

        # Create an empty array of length 20
        self.table = np.zeros(20, dtype=np.uint8)

        # Set the 4th, 13th and 14th value to 1
        # These are the Game of Life rules
        self.table[[3, 12, 13]] = 1

    def step(self):
        """Execute 1 step using the game's rules"""
        correlation = correlate2d(self.array, self.kernel, mode='same')
        self.array = self.table[correlation]


if __name__ == "__main__":
    size = 100
    life = Life(size)

    toad = ["0111",
            "1110"]
    glider_gun = ["000000000000000000000000010000000000",
                  "000000000000000000000011110000100000",
                  "000000000000010000000111100000100000",
                  "000000000000101000000100100000000011",
                  "000000000001000110000111100000000011",
                  "110000000001000110000011110000000000",
                  "110000000001000110000000010000000000",
                  "000000000000101000000000000000000000",
                  "000000000000010000000000000000000000"
                  ]

    life.add_cells(10, 10, glider_gun)

    life.save_gif("glider_gun", frames=150, fps=15)
