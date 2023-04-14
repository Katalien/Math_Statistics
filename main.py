import scipy.stats as sps
import numpy as np
import ipywidgets as widgets
import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns

def main():
    sample = np.random.normal(0, 1, 100)
    grid = np.linspace(-3, 3, 20)  # сетка для построения графика

    plt.figure(figsize=(12, 5))
    plt.hist(sample, bins=100, density=True,
             alpha=0.6, label='Гистограмма выборки')
    plt.plot(grid, sps.norm.pdf(grid), color='red',
             lw=5, label='Плотность случайной величины')
    plt.title(r'Случайная величина $\xi \sim \mathcal{N}$(0, 1)', fontsize=20)
    plt.legend(fontsize=14, loc=1)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
