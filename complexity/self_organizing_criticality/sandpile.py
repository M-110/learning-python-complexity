import numpy as np
import itertools
from scipy.signal import correlate2d
import matplotlib.pyplot as plt

from complexity.game_of_life.cell_2d import Cell2D


class SandPile(Cell2D):
    """Simulation of a sandpile using 2D cellular automata."""

    # The pattern of how to distribute grains of sand when one collapses.
    # 4 are removed from the center and distributed to the 4 neighbor piles.
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])

    def __init__(self, rows, cols=None, level=9):
        if cols is None:
            cols = rows
        self.array = np.ones((rows, cols), dtype=np.int32) * level
        self.toppled_sequence = []

    def step(self, k=3) -> int:
        """Apply one step of the sandpile rules.

        Returns the number of cells which collapsed."""
        # Find which cells are collapsing.
        is_toppling = self.grid > k
        toppled_count = np.sum(is_toppling)
        self.toppled_sequence.append(toppled_count)

        # Create correlation of where these collapsing cells should distribute
        # their grains of sand.
        correlation = correlate2d(is_toppling, self.kernel, mode='same',
                                  boundary='fill', fillvalue=0)

        # Apply the distribution
        self.grid += correlation

        return toppled_count

    def run(self):
        """Run simulation steps until thye sand pile is stable.

        returns number of steps ran and number of topples as a tuple pair"""
        total_toppled = 0
        for i in itertools.count(1):
            toppled_count = self.step()
            total_toppled += toppled_count
            if toppled_count == 0:
                return i, total_toppled

    def drop_random_grain(self):
        rows, cols = self.grid.shape
        random_cell = np.random.randint(rows), np.random.randint(cols)
        self.grid[random_cell] += 1

    def drop_and_run(self):
        """Drops a random grain and then runs until pile is stable"""
        self.drop_random_grain()
        return self.run()

    def draw_after_n_iterations(self, n):
        for i in range(n):
            print(i)
            self.drop_and_run()
        self.draw_grid(self.grid, cmap='Blues', alpha=.9, vmin=0, vmax=4, origin='upper')

    def animate_function(self, i):
        if i > 0:
            self.drop_and_run()
        print(i)
        self.draw()
        self.image.set_array(self.grid)

        return (self.image,)

    def print_topple_sequence(self):
        plt.plot(self.toppled_sequence)

    def draw_layers(self):
        plt.figure(figsize=(8, 8))
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            self.draw_grid(self.grid == i, cmap='Blues', alpha=.9, vmin=0, vmax=1, origin='upper')


if __name__ == "__main__":
    pile = SandPile(rows=200, level=12)

    # pile.run()

    # pile.draw_grid(pile.grid)
    # pile.draw_layers()

    # pile.draw_after_n_iterations(1500)       
    pile.save_gif(frames=500, fps=10)