import numpy as np
import distribution as ds
import os
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from statsmodels.distributions.empirical_distribution import ECDF

sample_sizes = [20, 60, 100]
filename = "lab4_res_empiric/"
filename2 = "lab4_res_kernel/"

def empiric():
    sizes = [20, 60, 100]
    if not os.path.isdir(filename):
        os.makedirs(filename)
    for name in ds.distributions:
        if name == "Poisson":
            interval = np.arange(6, 14, 1)
        else:
            interval = np.arange(-4, 4, 0.01)
        fig, ax = plt.subplots(1, 3, figsize=(12, 4))
        plt.subplots_adjust(wspace=0.5)
        fig.suptitle(name)
        for j in range(len(sizes)):
            arr = ds.get_sample(name, sizes[j])
            for a in arr:
                if name == "Poisson" and (a < 6 or a > 14):
                    arr = np.delete(arr, list(arr).index(a))
                elif name != "Poisson" and (a < -4 or a > 4):
                    arr = np.delete(arr, list(arr).index(a))

            ax[j].set_title("n = " + str(sizes[j]))
            if name == "Poisson":
                ax[j].step(interval, [ds.get_distr_func(name, x) for x in interval], color='#DDA0DD')
            else:
              ax[j].plot(interval, [ds.get_distr_func(name, x) for x in interval], color='#DDA0DD')
            if name == "Poisson":
                arr_ex = np.linspace(6, 14)
            else:
                arr_ex = np.linspace(-4, 4)
            ecdf = ECDF(arr)
            y = ecdf(arr_ex)
            ax[j].step(arr_ex, y, color='blue', linewidth=0.5)
            plt.savefig(filename + name + "_emperic.png")

def kernel():
    sizes = [20, 60, 100]
    if not os.path.isdir(filename2):
        os.makedirs(filename2)
    for name in ds.distributions:
        if name == "Poisson":
            interval = np.arange(6, 15, 1)
        else:
            interval = np.arange(-4, 4, 0.01)
        for j in range(len(sizes)):
            arr = ds.get_sample(name, sizes[j])
            for a in arr:
                if name == "Poisson" and (a < 6 or a > 14):
                    arr = np.delete(arr, list(arr).index(a))
                elif name != "Poisson" and (a < -4 or a > 4):
                    arr = np.delete(arr, list(arr).index(a))

            title = ["h = 1/2 * h_n", "h = h_n", "h = 2 * h_n"]
            bw = [0.5, 1, 2]
            fig, ax = plt.subplots(1, 3, figsize = (12, 4))
            plt.subplots_adjust(wspace = 0.5)
            for k in range(len(bw)):
                kde = gaussian_kde(arr, bw_method = 'silverman')
                h_n = kde.factor
                fig.suptitle(name + ", n = " + str(sizes[j]))
                ax[k].plot(interval, ds.get_density_func(name, interval), color='blue', alpha=0.5, label='density')
                ax[k].set_title(title[k])
                sns.kdeplot(arr, ax = ax[k], bw = h_n * bw[k], label = 'kde', color = 'black')
                ax[k].set_xlabel('x')
                ax[k].set_ylabel('f(x)')
                ax[k].set_ylim([0, 1])
                if name == 'Poisson':
                    ax[k].set_xlim([6, 14])
                else:
                    ax[k].set_xlim([-4, 4])
                ax[k].legend()
            plt.savefig(filename2 + name + "_kernel_n" + str(sizes[j]) + ".png")

def run_lab4():
    empiric()
    kernel()

def main():
    run_lab4()

if __name__ == '__main__':
    main()