"""This module saves visual representations of binary sequences.

The sequences are done through constant addition.
"""
import matplotlib.pyplot as plt
from binary_grapher import BinaryGrapher

class PrimeGrapher(BinaryGrapher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prime_iterator = self.prime_generator()
        self.sequence = []
    
    @staticmethod
    def prime_generator():
        """http://code.activestate.com/recipes/117119/"""
        D = {}
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1
            
    def step_function(self, n: int, i: int):
        x = next(self.prime_iterator)
        self.sequence.append(x)
        return x
        
if __name__ == "__main__":
    grapher = PrimeGrapher(1000000)
    grapher.generate_grid()
    #grapher.draw_graph()
    difference_sequence = [grapher.sequence[i+1] - grapher.sequence[i]
                           for i in range(len(grapher.sequence) - 2)]
    plt.plot(difference_sequence)
    print(max(difference_sequence))

#for i in range(1, 10):
#    grapher = BinaryGrapher(1000*i, step_size=i)
#    grapher.save_image(f'step_size_{i}', 'test', cmap='Greens')