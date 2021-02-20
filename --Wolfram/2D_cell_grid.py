import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class Cell2D:
    def __init__(self, width: int):
        self.width = width
        self.previous_layer = np.zeros((width, width), dtype=np.uint8)
        self.current_layer = np.zeros((width, width), dtype=np.uint8)
        self.current_layer[width//2][width//2] = 1
        
    def step(self):
        self.previous_layer = self.current_layer
        self.current_layer = np.zeros((self.width, self.width), dtype=np.uint8)
        
        for i in range(1, self.width-1):
            for j in range(1, self.width-1):
                neighbors = self.get_neighbors(i, j)
                self.apply_rules(i, j, *neighbors, switch=True)
                
    def get_neighbors(self, i, j) -> tuple:
        a = self.previous_layer[i-1][j]
        d = self.previous_layer[i][j+1]
        b = self.previous_layer[i+1][j]
        c = self.previous_layer[i][j-1]
        return a, b, c, d
    
    def apply_rules(self, i, j, a, b, c, d, switch=False):
        neighbor_sum = sum([a, b, c, d])
        if neighbor_sum == 1 or neighbor_sum == 4:
            if switch:
                self.current_layer[i][j] = -self.current_layer[i][j] + 1
            else:
                self.current_layer[i][j] = 1
        else:
            self.current_layer[i][j] = 0
    
    def run_n_steps(self, n):
        for _ in range(n):
            self.step()
        self.draw()
            
    def draw(self):
        self.image = plt.imshow(self.current_layer)
    
    def save_gif(self, filename='my_gif', frames=200, interval=.1, fps=30):
        writergif = animation.PillowWriter(fps=fps)
        self.animate_gif(frames, interval).save(filename+'.gif', 
                                                writer=writergif)
        
    def animate_gif(self ,frames, interval):
        fig = plt.gcf()
        self.draw()
        
        return animation.FuncAnimation(fig, self.animate_function,
                                       interval=interval,
                                       frames=frames)
    
    
    def animate_function(self, i):
        if i > 0:
            self.step()
            
        self.image.set_array(self.current_layer)
        
        return (self.image,)
        
        
        
    
    
cell = Cell2D(50)
cell.save_gif(frames=1000, fps=15)
            
