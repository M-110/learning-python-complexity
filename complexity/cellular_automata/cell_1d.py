"""An object-oriented implementation of cellular automata.

Uses rule 110 and a string as the initial conditions and saves
an image.

The class allows for random initial conditions, string-based initial conditions,
and a single square initial conditions.
"""

import matplotlib.pyplot as plt
import numpy as np
from binascii import a2b_base64


class Cell1D:
    """1D cellular automaton

    Args:
        rules: an integer that will be converted to a binary rule
        rows: number of rows for the graph
        columns: number of columns for the graph
    """

    # Window pattern for adding above numbers
    WINDOW = [4, 2, 1]

    def __init__(self, rules: int, rows: int, columns: int = None):
        if columns is None:
            columns = 2 * rows + 1
        self.rows = rows
        self.columns = columns

        self.array = np.zeros((rows, columns), dtype=np.int8)
        self.table = self.make_table(rules)

        self._current_row = 0

    def start_single(self):
        """Start with one cell in the top center"""
        self.array[0, self.columns // 2] = 1
        self._current_row += 1

    def start_random(self):
        """Start with each cell on the top row having a 50% probability of
        being active.
        """
        self.array[0] = np.random.random(self.columns).round()
        self._current_row += 1

    def start_string(self, string_: str):
        """Use a string as a random seed for the top row cells by converting
        the string into a binary value"""
        binary_string = ''.join(format(ord(char), 'b') for char in string_)
        string_to_int = [int(x) for x in binary_string]
        for i in range(min(len(self.array[0]), len(string_to_int))):
            self.array[0, i] = string_to_int[i]
        self._current_row += 1

    def make_table(self, rule: int):
        """Make table given the CA rule"""
        rule = np.array([rule], dtype=np.uint8)
        table = np.unpackbits(rule)[::-1]
        return table

    def loop(self, steps: int = 1):
        """Execute a given number of steps"""
        for i in range(steps):
            self.step()

    def step(self):
        """Computes the next row in the array"""
        c = np.correlate(self.array[self._current_row - 1], self.WINDOW, mode='same')
        self.array[self._current_row] = self.table[c]
        self._current_row += 1

    def plot_show(self):
        """Show the plot of the array"""
        plt.imshow(self.array, cmap='Blues', alpha=0.7)
        plt.xticks([])
        plt.yticks([])
        plt.savefig('Cell1D_ca_110.png')

    def draw_rows(self, n: int = None):
        """Calculate the rows and call the plot function"""
        if n is None:
            n = self.rows - 1
        else:
            n = min(self.rows - 1, n)

        self.loop(n)

        self.plot_show()


if __name__ == "__main__":
    initial_string = """
    Von Neumann cellular automata are the original expression of cellular automata,
    the development of which was prompted by suggestions made to John von Neumann by
    his close friend and fellow mathematician Stanislaw Ulam. Their original purpose
    was to provide insight into the logical requirements for machine self-replication,
    and they were used in von Neumann's universal constructor."""
    a = Cell1D(110, 200)
    a.start_string(initial_string)
    a.draw_rows()
