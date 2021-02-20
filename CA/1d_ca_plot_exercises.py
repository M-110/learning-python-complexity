import matplotlib.pyplot as plt
import numpy as np
from binascii import a2b_base64

class Cell1D:
    """1D cellular automaton
    
    Args:
        rule: an integer that will be converted to a binary rule
        rows: number of rows for the graph
        columns: number of columns for the graph
    """
    
    # Window pattern for adding above numbers
    WINDOW = [4, 2, 1]
    def __init__(self, rows: int, columns: int = None):
        if columns is None:
            columns = 2 * rows + 1
        self.rows = rows
        self.columns = columns
        
        self.array = np.zeros((rows, columns), dtype=np.int8)
        self.table = self.make_table()
        
        self._current_row = 0
        
    def start_single(self):
        """Start with one cell in the top center"""
        self.array[0, self.columns // 2] = 1
        self._current_row = 1
        
    def start_random(self):
        """Start with each cell on the top row having a 50% probability of
        being active.
        """
        self.array[0] = np.random.random(self.columns).round()
        self._current_row = 1
        
    def start_string(self, string_: str):
        """Use a string as a random seed for the top row cells by converting
        the string into a binary value"""
        binary_string = ''.join(format(ord(char), 'b') for char in string_)
        string_to_int = [int(x) for x in binary_string]
        for i in range(min(len(self.array[0]), len(string_to_int))):
            self.array[0, i] = string_to_int[i]
        self._current_row = 1
            
    def make_table(self, rule: int = 0):
        """Make table given the CA rule"""
        rule = np.array([rule], dtype=np.uint8)
        table = np.unpackbits(rule)[::-1]
        self.table = table
    
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
        
    def draw_rows(self, rule: int = 110, n: int = None):
        """Calculate the rows and call the plot function"""
        if n is None:
            n = self.rows - 1
        else:
            n = min(self.rows - 1, n)
        
        self.make_table(rule)
        
        self.loop(n)
        
        self.plot_show()
        
        
        
a = Cell1D(200)
a.start_single()
a.draw_rows(26)
        
    