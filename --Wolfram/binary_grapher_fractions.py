"""This module saves visual representations of binary sequences.

The sequences are done through constant addition.
"""
import matplotlib.pyplot as plt
from binary_grapher import BinaryGrapher
from decimal import Decimal, getcontext

class FractionGrapher(BinaryGrapher):
    def __init__(self, *args, numerator, divisor, **kwargs):
        super().__init__(*args, **kwargs)
        getcontext().prec = 2_000
        fraction = Decimal(numerator) / Decimal(divisor)
        self.fraction_iter = iter(str(fraction)[2:].ljust(500, '0'))
            
    def step_function(self, n: int, i: int):
        print(i)
        x = int(next(self.fraction_iter))
        return x
    
    def fill_grid(self):
        width = max(len(row) for row in self.grid)
        for i in range(len(self.grid)):
            padding = width - len(self.grid[i])
            self.grid[i] += [0] * padding
        
if __name__ == "__main__":
    #grapher = FractionGrapher(100, numerator=9, divisor=13)
    #grapher.draw_graph()
    
    # Generate random stuff
    for i in range(50):
        divisor = randint(2,100)
        numerator = randint(1, divisor)
        grapher = FractionGrapher(100, numerator=numerator, divisor=divisor)
        grapher.save_image(f'random_{numerator}_over_{divisor}', 'division', cmap='Greens')

     for i in range(1, 100):
         grapher = FractionGrapher(100, numerator=1, divisor=i)
         grapher.save_image(f'1_over_{i}', 'division', cmap='Greens')