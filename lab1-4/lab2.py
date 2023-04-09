import distribution as ds
import numpy as np
import os
from math import *

samle_sizes = [10, 50, 1000]
repeats = 1000

def count_mean(sample, n):
    return sum(sample)/n

def cont_median(sample, n):
    srt_sample = sample.sort()
    if n % 2 == 0:
        return (srt_sample[n/2] + srt_sample[n/2+1])/2
    else:
        return srt_sample[(n+1)/2]

def count_z_r(sample, n):
    return (sample[0] + sample[n-1])/2

def count_quart(sample, p):
    new_sample = np.sort(sample)
    k = len(sample) * p
    if k.is_integer():
        return new_sample[int(k)]
    else:
        return new_sample[int(k) + 1]

def count_z_q(sample):
    return (count_quart(sample, 0.25) + count_quart(sample, 0.75)) / 2

def count_z_tr(sample, n):
    r = int(n/4)
    res = 0
    for i in range(r+1, n-r+1):
        res += sample[i]
    return res/(n - 2*r)

def count_dispersion(sample, n):
    np.around(np.mean(np.multiply(sample, sample)) - np.mean(sample) * np.mean(sample), decimals=4),


def count_stat_characteristics():
    mean, median, z_r, z_q, z_tr = [], [], [], [], []

def count_table_res():
    if not os.path.isdir("lab2_res/"):
        os.makedirs("lab2_res/")
    mean, median, z_r, z_q, z_tr = [], [], [], [], []
    for dist in ds.distributions:
        for size in samle_sizes:
            for i in range(repeats):
                sample = ds.get_sample(dist, size)
                mean.append(count_mean(sample, size))
                median.append(count_mean(sample, size))
                z_r.append(count_z_r(sample, size))
                z_q.append(count_z_q(sample))
                z_tr.append(count_z_tr(sample, size))
            with open("lab2_res/" + dist + str(size) + ".tex", "w") as f:
                f.write("\\begin{tabular}{|c|c|c|c|c|c|}\n")
                f.write("\\hline\n")
                f.write("& \\bar{x} & mediana & z_r & z_Q & z_tr & \\\\\n")
                f.write("E(z) & " + f"{np.around(np.mean(mean), decimals=4)} & "
                                    f"{np.around(np.mean(median), decimals=4)} & "
                                    f"{np.around(np.mean(z_r), decimals=4)} & "
                                    f"{np.around(np.mean(z_q), decimals=4)} & "
                                    f"{np.around(np.mean(z_tr), decimals=4)} & \\\\\n")
                f.write("\\hline\n")
                f.write(
                    "D(z) & " + f"{np.around(np.mean(np.multiply(mean, mean)) - np.mean(mean) * np.mean(mean), decimals=4)} & "
                                f"{np.around(np.mean(np.multiply(median, median)) - np.mean(median) * np.mean(median), decimals=4)} & "
                                f"{np.around(np.mean(np.multiply(z_r, z_r)) - np.mean(z_r) * np.mean(z_r), decimals=4)} & "
                                f"{np.around(np.mean(np.multiply(z_q, z_q)) - np.mean(z_q) * np.mean(z_q), decimals=4)} & "
                                f"{np.around(np.mean(np.multiply(z_tr, z_tr)) - np.mean(z_tr) * np.mean(z_tr), decimals=4)} & \\\\\n")
                f.write("\\end{tabular}")




def run_lab2():
    for dist in ds.distributions:
        for size in samle_sizes:
            sample = ds.get_sample(dist)

def main():
    count_table_res()

if __name__ == '__main__':
    main()