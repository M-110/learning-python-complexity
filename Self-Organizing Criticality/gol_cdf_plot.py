from sandpile import SandPile
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
from empiricaldist import Pmf, Cdf
from game_of_life_helper import Life
from random import randint



def generate_time_and_duration(n=10000):
    size = 50
    life = Life(size)
    for i in range(size):
        for j in range(size):
            life.make_life(i,j,str(randint(0,1)))
            
    
    
    # **WARNING** This takes a few minutes
    res = life.run_n_iterations(n)
    T, S = res
    
    T = np.array(T)
    S = np.array(S)
    #T, S = np.transpose(res)
    
    T = T[T>3]
    S = S[S>10]
    print(S, len(S))
    return T, S

def plot_pmf(T, S):
    pmfT = Pmf.from_seq(T)
    pmfS = Pmf.from_seq(S)
    
    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)a
    pmfT.plot(xlim=(0,50), xlabel="Avalanche duration", ylabel="PMF")
    
    
    plt.subplot(1, 2, 2)
    pmfS.plot(title="Game of Life PMF", xlim=(0,100), xlabel="Avalanche size", ylabel="PMF")
    plt.show('PMF size and duration')
    
    fig.savefig("pmf_gol_plot.png")
    
def plot_cdf(T, S):
    cdfT = Cdf.from_seq(T)
    cdfS = Cdf.from_seq(S)
    
    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    cdfT.plot(xlim=(0,50), xlabel="Avalanche duration", ylabel="CDF")
    
    
    plt.subplot(1, 2, 2)
    cdfS.plot(title="Game of Life CDF", xlim=(0,5000), xlabel="Avalanche size", ylabel="CDF")
    plt.show('PMF size and duration')
    
    fig.savefig("cdf_gol_plot.png")
    
    
if __name__ == "__main__":
    T, S = generate_time_and_duration(5900)
    #plot_cdf(T, S)
    plot_pmf(T, S)