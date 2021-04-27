import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate2d

from complexity.game_of_life.cell_2d import Cell2D


class ReactionDiffusion(Cell2D):
    kernel = np.array([[.05, .2, .05],
                       [.2, -1, .2],
                       [.05, .2, .05]])

    def __init__(self, rows, cols, ra, rb, f, k, noise=0.1):
        super().__init__(rows)
        self.rows = rows
        self.cols = cols
        self.ra = ra  # diffusion rate of a
        self.rb = rb  # diffusion rate of b
        self.f = f  # feed rate
        self.k = k  # kill rate
        self.array_a = np.ones((rows, cols), dtype=float)
        self.array_b = noise * np.random.random((rows, cols))
        self.add_island()

    def step(self):
        A = self.array_a
        B = self.array_b

        correlation_A = correlate2d(A, self.kernel, mode='same', boundary='wrap')
        correlation_B = correlate2d(B, self.kernel, mode='same', boundary='wrap')

        reaction = A * B ** 2
        self.array_a += self.ra * correlation_A - reaction + self.f * (1 - A)
        self.array_b += self.rb * correlation_B + reaction - (self.f + self.k) * B

    def draw(self):
        """Draw the reaction."""
        plt.axis([0, self.rows, 0, self.cols])
        plt.xticks([])
        plt.yticks([])
        shared_options = dict(interpolation='bicubic', vmin=None, vmax=None, alpha=0.3,
                              origin='upper', extent=[0, self.rows, 0, self.cols])
        plt.imshow(self.array_a, cmap='twilight', **shared_options)
        plt.imshow(self.array_b, cmap='cool', **shared_options)
        self.image = plt.gci()

    def animate_function(self, i):
        if i > 0:
            for i in range(100):
                self.step()
        self.draw()
        return self.image,

    def add_island(self, height=0.1):
        rows, cols = self.array_b.shape
        radius = min(rows, cols) // 20
        i = rows // 2
        j = cols // 2
        self.array_b[(i - radius):(i + radius), (j - radius):(j + radius)] += height


if __name__ == '__main__':
    diffusion = ReactionDiffusion(100, 100, 0.5, 0.25, 0.035, 0.062)
    # for _ in range(500):
    #     diffusion.step()
    # diffusion.draw()
    # plt.show()
    # diffusion.add_cells(7, 7, ['111', '111', '111'])
    # pairs = [(0.0354, 0.057),  # X
    #          (0.055, 0.062),  # X
    #          (0.039, 0.065),  # OO
    #          (0.1, 0.002),
    #          (0.04, 0.035),
    #          (0.02, 0.085),
    #          (0.065, 0.043)]
    # pairs = [(0.043, 0.055),
    #          (0.039, 0.064),
    #          (0.042, 0.069)]
    pairs = [(0.012, 0.032),
             (0.034, 0.066)]
    for f, k in pairs:
        diffusion = ReactionDiffusion(100, 100, 0.5, 0.26, f, k)
        diffusion.save_gif(filename=f'X_reaction_diffusion_f_{f}_k_{k}_long', frames=150, fps=10)
