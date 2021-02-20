from typing import Tuple
from random import randint
from cell import Cell2D
import numpy as np
from nptyping import NDArray
import matplotlib.pyplot as plt


def distances_from(n: int, i: int, j: int) -> NDArray:
    """Returns an array of distances from location (i, j)."""
    X, Y = np.indices((n, n))
    return np.hypot(X - i, Y - j)


def make_locs(n, m) -> NDArray:
    """Makes an array for locations for an n x m grid."""
    return np.array([[i, j] for i in range(n) for j in range(m)])


def find_visible_locs(vision: int) -> NDArray:
    def make_array(d):
        a = np.array([[-d, 0], [d, 0], [0, -d], [0, d]])
        np.random.shuffle(a)
        return a
    
    arrays =[make_array(d) for d in range(1, vision + 1)]
    return np.vstack(arrays)


class Agent:
    """Agent created as specific location with attributes randomized by the 
    paramaters."""
    
    # Default parameters
    max_vision=6
    max_metabolism=4
    min_lifespan=10_000
    max_lifespan=10_000
    min_sugar=5
    max_sugar=25
    
    def __init__(self, loc: Tuple[int, int], env, params: dict):
        self.loc = tuple(loc)
        self.env = env
        self.age = 0
        
        # Update default paramaters with any passed to init
        for key, value in params.items():
            setattr(self, key, value)
            
        self.vision = randint(1, self.max_vision+1)
        self.metabolism = randint(1, self.max_metabolism)
        self.lifespan = randint(self.min_lifespan, self.max_lifespan)
        self.sugar = randint(self.min_sugar, self.max_sugar)
        
    def step(self, env):
        self.loc = self.env.look_and_move(self.loc, self.vision)
        self.sugar += self.env.harvest(self.loc) - self.metabolism
        self.age += 1
        
    @property
    def is_starving(self) -> bool:
        return self.sugar < 0
    
    @property
    def is_old(self) -> bool:
        return self.age > self.lifespan


class Sugarscape(Cell2D):
    def __init__(self, n, **params):
        self.n = n
        self.params = params
        
        self.agent_count_seq = []
        self.capacity = self.make_capacity()
        self.grid = self.capacity.copy()
        self.make_agents()
        
    def make_capacity(self) -> NDArray:
        dist1 = distances_from(self.n, 15, 15)
        dist2 = distances_from(self.n, 35, 35)
        dist = np.minimum(dist1, dist2)
        bins = [21, 16, 11, 6]
        return np.digitize(dist, bins)
        
    
    def make_agents(self):
        n, m = self.params.get('starting_box', self.grid.shape)
        locs = make_locs(n, m)
        np.random.shuffle(locs)
        
        num_agents = self.params.get('num_agents', 400)
        self.agents = [Agent(locs[i], self, self.params) 
                       for i in range(num_agents)]
        
        self.occupied = {agent.loc for agent in self.agents}
        
    def grow(self):
        grow_rate = self.params.get('grow_rate', 1)
        self.grid = np.minimum(self.grid + grow_rate, self.capacity)
        
    def look_and_move(self, center, vision) -> Tuple[int, int]:
        """Returns closest to center cell with the most sugar within vision
        distance.
        """
        locs = find_visible_locs(vision)
        locs = (locs + center) % self.n
        locs = [tuple(loc) for loc in locs]
        empty_locs = [loc for loc in locs if loc not in self.occupied]
        
        if len(empty_locs) == 0:
            return center
        
        t = [self.grid[loc] for loc in empty_locs]
        
        closest_i = np.argmax(t)
        return empty_locs[closest_i]
    
    def harvest(self, loc: Tuple[int, int]):
        """Removes and returns sugar for loc."""
        sugar = self.grid[loc]
        self.grid[loc] = 0
        return sugar
    
    def step(self):
        replace = self.params.get('replace', False)
        
        random_order = np.random.permutation(self.agents)
        for agent in random_order:
            self.occupied.remove(agent.loc)
            agent.step(self)
            if agent.is_starving or agent.is_old:
                self.agents.remove(agent)
                if replace:
                    self.add_agent()
            else:
                self.occupied.add(agent.loc)
                
        self.agent_count_seq.append(len(self.agents))
        
        self.grow()
        return len(self.agents)
    
    def add_agent(self) -> Agent:
        new_agent = Agent(self.random_loc(), self.params)
        self.agents.append(new_agent)
        self.occupied.add(new_agent.loc)
        return new_agent
    
    def random_loc(self) -> Tuple[int, int]:
        while True:
            loc = tuple(np.random.randint(self.n, size=2))
            if loc not in self.occupied:
                return loc
            
    def draw(self):
        fig = plt.figure()
        x, y = self.get_coords()
        self.points = plt.plot(x, y, '.', color='red')[0]
        self.image = self.draw_grid(self.grid, origin='lower')
        return fig
        
    def get_coords(self) -> Tuple[int, int]:
        rows, cols = np.transpose([agent.loc for agent in self.agents])
        return cols + .5, rows + .5
    

env = Sugarscape(50, num_agents=400)
env.save_gif('babycat')
