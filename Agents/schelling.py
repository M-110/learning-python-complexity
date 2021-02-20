import numpy as np
from scipy.signal import correlate2d
from typing import Tuple, List
from nptyping import NDArray
from cell import Cell2D
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

Grid = NDArray
Location = Tuple[int, int]

palette = sns.color_palette('muted')
colors = 'white', palette[1], palette[0]
cmap = LinearSegmentedColormap.from_list('cmap', colors)

class Schelling(Cell2D):
    """Schelling model grid.
    
    Args:
        n: number or rows in grid.
        p: threshold of similar neighbors for not moving."""
    
    kernel = np.array([[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1]], dtype=np.int8)
    
    def __init__(self, n: int, p: float):
        self.p = p
        choices = [0, 1, 2]
        
        # 10% of homes are empty, 45% are 1, 45% are 2
        probs = [0.1, 0.45, 0.45]
        self.grid: Grid[int] = np.random.choice(choices, (n, n), p=probs)
        self.image = None
        
    def count_neighbors(self) -> Tuple[Grid[bool], Grid[float], Grid[float], Grid[float]]:
        """Count the neighbors and the fraction of their neighbors.
        
        Returns:
            empty: Grid with 1s in cells that are empty
            frac_red: Grid with fraction of neighbors that are red
            frac_blue: Grid with fraction of neighbors that are blue
            frac_same: Grid with fraction of neighbors that are the same"""
        empty: Grid[bool] = self.grid == 0
        red: Grid[bool]  = self.grid == 1
        blue: Grid[bool]  = self.grid == 2
        
        
        num_red: Grid[int] = correlate2d(red, self.kernel,
                                         mode='same', boundary='wrap')
        num_blue: Grid[int] = correlate2d(blue, self.kernel,
                                          mode='same', boundary='wrap')
        
        num_neighbors: Grid[int] = num_red + num_blue
        frac_red: Grid[float] = num_red / num_neighbors
        frac_blue: Grid[float] = num_red / num_neighbors
        
        frac_same: Grid[float] = np.where(red, frac_red, frac_blue)
        frac_same[empty] = np.nan
        
        return empty, frac_red, frac_blue, frac_same
    
    def get_segregation_fraction(self) -> float:
        """Returns average fraction of similar nieghbors."""
        *_, frac_same = self.count_neighbors()
        return np.nanmean(frac_same)
    
    @staticmethod
    def locations_where(condition: Grid[bool]) -> List[Location]:
        return list(zip(*np.nonzero(condition)))
        
    def step(self) -> float:
        """Exceutes one step.
        
        Return:
            Average fraction of similar neighbors."""
        empty, *_, frac_same = self.count_neighbors()
        
        unhappy: Grid[bool] = frac_same < self.p
        unhappy_locations: List[Location] = self.locations_where(unhappy)
        
        empty_locations: List[Location] = self.locations_where(empty)
        
        np.random.shuffle(unhappy_locations)
        
        num_empty = np.sum(empty)
        
        for source in unhappy_locations:
            # Random empty destination.
            i = np.random.randint(num_empty)
            destination: Location = empty_locations[i]
            
            # Move source to destination.
            self.grid[destination] = self.grid[source]
            self.grid[source] = 0
            
            # Change empty location from destination to source.
            empty_locations[i] = source
            
        return np.nanmean(frac_same)
    
    def draw(self):
        """Draw cells."""
        self.image = self.draw_grid(self.grid, cmap=cmap, vmax=2)
    

s = Schelling(10, .3)
for i in range(5000):
    s.step()
    print(s.get_segregation_fraction())
s.draw()
