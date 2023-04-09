import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import distribution as ds
import os
import seaborn as sns
import pandas as pd

filename = "lab3_plots/"
filename2 = "lab3_res/"
sample_size = [20, 100]
repeats = 1000

def draw_boxplot(dist_name):
    if not os.path.isdir(filename):
        os.makedirs(filename)
    data_dict = {}
    fig, ax = plt.subplots()
    for size in sample_size:
        key = "n =" + str(size)
        data_dict[key] = ds.get_sample(dist_name, size)
    df = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in data_dict.items()]))
    sns.boxplot(data=df, orient="v", ax=ax).set_title(dist_name)
    plt.savefig(filename + dist_name + ".png")

def find_min_boarder(sample):
    return np.quantile(sample, 0.25) - 1.5 * (np.quantile(sample, 0.75) - np.quantile(sample, 0.25))

def find_max_boarder(sample):
    return np.quantile(sample, 0.25) + 1.5 * (np.quantile(sample, 0.75) - np.quantile(sample, 0.25))

def count_outline_proportion(sample, min_val, max_val):
    res = 0
    for el in sample:
        if el < min_val or el > max_val:
            res += 1
    return res

def count_outliers():
    if not os.path.isdir(filename2):
        os.makedirs(filename2)
    rows = []
    for dist in ds.distributions:
        for size in sample_size:
            proportion = 0
            for _ in range(repeats):
                sample = ds.get_sample(dist, size)
                min_val = find_min_boarder(sample)
                max_val = find_max_boarder(sample)
                proportion += count_outline_proportion(sample, min_val, max_val)
            proportion /= repeats
            rows.append(dist + " n = $" + str(size) + "$ & $" + str(np.around(proportion / size, decimals=3)) + "$")
    with open(filename2 +"outliers.tex", "w") as f:
        f.write("\\begin{tabular}{|c|c|}\n")
        f.write("\\hline\n")
        f.write("Sample & Share of emissions \\\\\n")
        f.write("\\hline\n")
        for row in rows:
            f.write(row + "\\\\\n")
            f.write("\\hline\n")
        f.write("\\end{tabular}")

def run_lab3():
    # for dist in ds.distributions:
    #     draw_boxplot(dist)
    count_outliers()


def main():
    run_lab3()

if __name__ == '__main__':
    main()