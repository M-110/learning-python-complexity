import matplotlib.pyplot as plt
import numpy as np
from math import floor, ceil

a = lambda x: sum(x)/3, [1,1,1]
b = lambda x: sum(x[:2])/3, [1,1,0]
c = lambda x: (x[0] + x[2])/2, [1,0,1]
d = lambda x: x[0], [1,0,0]
e = lambda x: sum(x[1:])/2, [0,1,1]
f = lambda x: x[1], [0,1,0]
g = lambda x: x[2], [0,0,1]
h = lambda x: 1, [0,0,0]

rule_table = a,b,c,d,e,f,g,h

def apply_rule(n, row):
    rules = bin(n)[2:].rjust(8, '0')
    output = 0
    applied_rules = [rule_table[i] for i, rule in enumerate(rules) if rule == '1']
    for rule in applied_rules:
        if all(int(ceil(row[i])) == rule[1][i] for i in range(3)):
            output = rule[0]([row[i]*rule[1][i] for i in range(3)])
            return output
    return output


output = apply_rule(122, [.5, .3, .6])

rows = 100
cols = rows
rule_number = 137

grid = np.zeros((rows, cols), dtype=float)

grid[0,rows//2] = 1

for i in range(1, rows):
    for j in range(2, cols-2):
        new_value = apply_rule(rule_number, [grid[i-1, j-1], grid[i-1, j], grid[i-1, j+1]])
        
        if new_value > 1:
            new_value = new_value - floor(new_value) 
        grid[i, j] = new_value
                
        

plt.imshow(grid, cmap='twilight')
#plt.imshow(grid, cmap='Greys')