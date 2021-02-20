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

def recursive(n: int, func, f: list = None) -> list:
    if f is None:
        f = [1, 1]
    else:
        f = f[:]
        
    for i in range(len(f), n):
        f.append(func(i, f))
    return f
        

# The Python syntax for defining these recursive functions is actually
# identical to the traditional way you'd write them out so they self-document.

# The first if block is the initial conditions for that function.

# The return statement is the recursive formula being used.

def func_a(n: int, f: list) -> int:
    return 1 + f[n - f[n - 1]]


def func_b(n: int, f: list) -> int:
    return 2 + f[n - f[n - 1]]


def func_c(n: int, f: list) -> int:
    return f[f[n - 1]] + f[n - f[n-1]]


def func_d(n: int, f: list) -> int:
    return f[n - f[n - 1]] + f[n - f[n - 2] - 1]


def func_e(n: int, f: list) -> int:
    return f[n - f[n - 1]] + f[n - f[n - 2]]


def func_f(n: int, f: list) -> int:
    return f[n - f[n - 1] - 1] + f[n - f[n - 2] - 1]


def func_g(n: int, f: list) -> int:
    return f[f[n - 1]] + f[n - f[n - 2] - 1]


def func_h(n: int, f: list) -> int:
    return f[f[n - 1]]  + f[n - 2 * f[n - 1] + 1]

def func_i(n: int, f: list) -> int:
    return f[n-f[n-1]-1] + f[n-f[n-2]-1]

def func_j(n: int, f: list) -> int:
    return f[f[n-1]] + f[n - f[n-2]-1]

def func_fib(n: int, f: list) -> int:
    return f[n-1] + f[n-2]


    

    
a = recursive(100, func_a, f=[1])
b = recursive(100, func_b)
c = recursive(100, func_c)
d = recursive(10000, func_d)
e = recursive(10000, func_e)
f = recursive(100, func_f)
g = recursive(100, func_g)
#h = recursive(100, func_h)
i = recursive(2000, func_i)
j = recursive(1000, func_j)
fib = recursive(100, func_fib)




plt.plot([y- x/2 for x, y in enumerate(e, start=1)])
