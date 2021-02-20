
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
from random import randint

def generate_array(rows, cols):
    """Create a 2d array"""
    array = np.zeros((rows, cols), dtype=np.uint8)
    return array

def step(array, i, window=[4,2,1]):
    previous_row = array[i-1]
    c = np.correlate(previous_row, window, mode='same')
    array[i] = table[c]
    
def make_table(rule):
    rule = np.array([rule], dtype=np.uint8)
    table = np.unpackbits(rule)[::-1]
    return table

table = make_table(110)
        
def step_over_all_rows(array, step_function):
    # Iterate through all rows in the array
    for i in range(1, array.shape[0]):
        step_function(array, i)
    plt.imshow(array)
    
rows = 500
cols = 1000
    
# Create an array 
array = generate_array(rows, cols)

#set initial conditions
array[0,500] = 1


step_over_all_rows(array, step)