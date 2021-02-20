"""This module saves visual representations of binary sequences.

The sequences are done through constant addition.
"""
import matplotlib.pyplot as plt
from binary_grapher import BinaryGrapher
from decimal import Decimal, getcontext
from random import randint

class RootGrapher(BinaryGrapher):
    def __init__(self, *args, value, **kwargs):
        super().__init__(*args, **kwargs)
        getcontext().prec = 2_000
        sqrt_decimal = Decimal(value).sqrt()
        str_sqrt = str(sqrt_decimal)
        if '.' not in str_sqrt:
            str_sqrt = '0.' + '0'*50000
        self.sqrt_iter = iter(str_sqrt.split('.')[1])
            
    def step_function(self, n: int, i: int):
        x = int(next(self.sqrt_iter))
        return x
    
    def fill_grid(self):
        width = max(len(row) for row in self.grid)
        for i in range(len(self.grid)):
            padding = width - len(self.grid[i])
            self.grid[i] += [0] * padding
        
if __name__ == "__main__":
    grapher = RootGrapher(100, value=7)
    grapher.draw_graph()
    
    
    for i in range(2, 100):
        grapher = RootGrapher(100, value=i)
        grapher.save_image(f'sqrt({i})', 'root', cmap='Greens')
    