import distribution as ds
import numpy as np
import os
from math import *

samle_sizes = [10, 50, 1000]
repeats = 1000

def count_mean(sample, n):
    return sum(sample)/n

def count_median(sample, n):
    srt_sample = sorted(sample)
    if n % 2 == 0:
        return (srt_sample[int(n/2)] + srt_sample[int(n/2+1)])/2
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

    for dist in ds.distributions:
        for size in samle_sizes:
            mean, mediana, z_r, z_q, z_tr = [], [], [], [], []
            for i in range(repeats):
                sample = ds.get_sample(dist, size)
                mean.append(count_mean(sample, size))
                mediana.append(count_median(sample, int(size)))
                z_r.append(count_z_r(sample, size))
                z_q.append(count_z_q(sample))
                z_tr.append(count_z_tr(sample, size))

            E_mean = np.around(np.mean(mean), decimals=4)
            E_mediana = np.around(np.mean(mediana), decimals=4)
            E_z_r = np.around(np.mean(z_r), decimals=4)
            E_z_Q = np.around(np.mean(z_q), decimals=4)
            E_z_tr = np.around(np.mean(z_tr), decimals=4)

            D_mean = np.around(np.mean(np.multiply(mean, mean)) - np.mean(mean) * np.mean(mean), decimals=4)
            D_mediana = np.around(np.mean(np.multiply(mediana, mediana)) - np.mean(mediana) * np.mean(mediana), decimals=4)
            D_z_r =  np.around(np.mean(np.multiply(z_r, z_r)) - np.mean(z_r) * np.mean(z_r), decimals=4)
            D_z_Q =   np.around(np.mean(np.multiply(z_q, z_q)) - np.mean(z_q) * np.mean(z_q), decimals=4)
            D_z_tr =  np.around(np.mean(np.multiply(z_tr, z_tr)) - np.mean(z_tr) * np.mean(z_tr), decimals=4)

            with open("lab2_res/" + dist + str(size) + ".tex", "w") as f:
                f.write("\\begin{tabular}{|c|c|c|c|c|c|}\n")
                f.write("\\hline\n")
                f.write("& \\overline{x} & mediana & z_r & z_Q & z_tr & \\\\\n")
                f.write("\\hline\n")
                f.write("E(z) & " + f"{E_mean} & "
                                    f"{E_mediana} & "
                                    f"{E_z_r} & "
                                    f"{E_z_Q} & "
                                    f"{E_z_tr} & \\\\\n")
                f.write("\\hline\n")
                f.write(
                    "D(z) & " + f"{D_mean} & "
                                f"{D_mediana} & "
                                f"{D_z_r} & "
                                f"{D_z_Q} & "
                                f"{D_z_tr} & \\\\\n")
                f.write("\\hline\n")

                mean_left, mean_right = np.around(E_mean - sqrt(D_mean), decimals=4), np.around(E_mean + sqrt(D_mean), decimals=4)
                mediana_left, mediana_right = np.around(E_mediana - sqrt(D_mediana), decimals=4), np.around(E_mediana + sqrt(D_mediana), decimals = 4)
                z_r_left, z_r_right = np.around(E_z_r - sqrt(D_z_r), decimals=4), np.around(E_z_r + sqrt(D_z_r), decimals = 4)
                z_q_left, z_q_right = np.around(E_z_Q - sqrt(D_z_Q), decimals=4), np.around(E_z_Q + sqrt(D_z_Q), decimals=4)
                z_tr_left, z_tr_right = np.around(E_z_tr - sqrt(D_z_tr), decimals=4), np.around(E_z_tr + sqrt(D_z_tr), decimals=4)

                f.write(
                    "E(x) - \sqrt(D(z)) & " + f"{mean_left} & "
                                              f"{mediana_left} & "
                                              f"{z_r_left} & "
                                              f"{z_q_left} & "
                                              f"{z_tr_left} & \\\\\n")

                f.write("\\hline\n")
                f.write(
                    "E(x) + \sqrt(D(z)) & " + f"{mean_right} & "
                                f"{mediana_right} & "
                                f"{z_r_right} & "
                                f"{z_q_right} & "
                                f"{z_tr_right} & \\\\\n")
                f.write("\\hline\n")


                mean_point = round((mean_left + mean_right)/2)
                mediana_point = round((mediana_left + mediana_right)/2)
                z_r_point = round((z_r_left + z_r_right)/2)
                z_q_point = round((z_q_left + z_q_right)/2)
                z_tr_point = round((z_tr_left + z_tr_right)/2)

                f.write(
                    "\n$\hat{E}$ & " + f"{mean_point} & "
                                              f"{mediana_point} & "
                                              f"{z_r_point} & "
                                              f"{z_q_point} & "
                                              f"{z_tr_point} & \\\\\n")

                f.write("\\hline\n")
                f.write("\\end{tabular}")

def run_lab2():
    for dist in ds.distributions:
        for size in samle_sizes:
            sample = ds.get_sample(dist)

def main():
    count_table_res()

if __name__ == '__main__':
    main()