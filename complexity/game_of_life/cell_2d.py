from abc import abstractmethod
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class Cell2D:
    """Implementation of a 2D CA.
    
    Args:
        n: number of rows
        m: number of columns
    """

    def __init__(self, n, m=None):
        if m is None:
            m = n
        self.array = np.zeros((n, m), np.uint8)
        self.image = None
        self.plot_options = None
        self.set_plot_options()

    def set_plot_options(self, cmap='Blues', alpha=1, vmin=0, vmax=4,
                         interpolation='nearest', origin='upper'):
        self.plot_options = dict(cmap=cmap, alpha=alpha, vmin=vmin, vmax=vmax,
                                 interpolation=interpolation, origin=origin)

    def add_cells(self, row, col, values):
        """Add cells using the given values at beginning
        at the row/column location.
        
        Args:
            row: index of the row
            col: index of the col
            values: strings containing 1s and 0s
        """
        for i, value in enumerate(values):
            self.array[row + i, col:col + len(value)] = np.array([int(x) for x in value])

    @abstractmethod
    def step(self):
        """One step."""
        ...

    def draw(self):
        """Draw the grid"""
        g = self.array.copy()
        
        # Get width/height of grid for plotting
        x, y = g.shape
        plt.axis([0, x, 0, y])
        plt.xticks([])
        plt.yticks([])

        self.image = plt.imshow(g, **self.plot_options)

    def animation_init_function(self):
        print('Beginning animation.')

    def animate_function(self, i):
        if i > 0:
            self.step()

        self.image.set_array(self.array)

        return self.image,

    def animate_gif(self, frames, interval):
        fig = plt.gcf()
        self.draw()

        return animation.FuncAnimation(fig, self.animate_function,
                                       init_func=self.animation_init_function,
                                       frames=frames, interval=interval)

    def save_gif(self, filename='my_gif', frames=300, interval=1, fps=30):
        writer_gif = animation.PillowWriter(fps=fps)
        self.animate_gif(frames, interval).save(f'{filename}.gif',
                                                writer=writer_gif)
        print(f'Saved gif as "{filename}.gif".')
