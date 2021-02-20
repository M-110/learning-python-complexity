from sandpile import SandPile
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
from empiricaldist import Pmf, Cdf



def generate_time_and_duration(n=10000):
    pile = SandPile(rows=50, level=30)
    pile.run()
    
    # **WARNING** This takes a few minutes
    res = [pile.drop_and_run() for i in range(n)]
    
    T, S = np.transpose(res)
    
    T = T[T>1]
    S = S[S>1]
    
    return T, S

def plot_pmf(T, S):
    pmfT = Pmf.from_seq(T)
    pmfS = Pmf.from_seq(S)
    
    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    pmfT.plot(xlim=(0,50), xlabel="Avalanche duration", ylabel="PMF")
    
    
    plt.subplot(1, 2, 2)
    pmfS.plot(xlim=(0,50), xlabel="Avalanche size", ylabel="PMF")
    plt.show('PMF size and duration')
    
    fig.savefig("pmf_plot.png")
    
def plot_cdf(T, S):
    cdfT = Cdf.from_seq(T)
    cdfS = Cdf.from_seq(S)
    
    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    cdfT.plot(xlim=(0,50), xlabel="Avalanche duration", ylabel="CDF")
    
    
    plt.subplot(1, 2, 2)
    cdfS.plot(xlim=(0,50), xlabel="Avalanche size", ylabel="CDF")
    plt.show('PMF size and duration')
    
    fig.savefig("cdf_plot.png")
    
    
if __name__ == "__main__":
    T, S = generate_time_and_duration(100000)
    plot_cdf(T, S)
    plot_pmf(T, S)