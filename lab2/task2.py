import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import minimize

filename = "task2_data/"
size = 20

def least_squares_coefs(x, y):
    xy_m = np.mean(np.multiply(x, y))
    x_m = np.mean(x)
    x_2_m = np.mean(np.multiply(x, x))
    y_m = np.mean(y)
    b1_mnk = (xy_m - x_m * y_m) / (x_2_m - x_m * x_m)
    b0_mnk = y_m - x_m * b1_mnk

    return b0_mnk, b1_mnk

def abs_dev_val(b_arr, x, y):
    return np.sum(np.abs(y - b_arr[0] - b_arr[1] * x))

def linear_approx_coefs(x, y):
    init_b = np.array([0, 1])
    res = minimize(abs_dev_val, init_b, args=(x, y), method='COBYLA')
    return res.x

def draw(lsm_0, lsm_1, lam_0, lam_1, x, y, title, fname):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', s=6, label='Выборка')
    y_lsm = np.add(np.full(20, lsm_0), x * lsm_1)
    y_lam = np.add(np.full(20, lam_0), x * lam_1)
    y_real = np.add(np.full(20, 2), x * 2)
    ax.plot(x, y_lsm, color='blue', label='МНК')
    ax.plot(x, y_lam, color='red', label='МНМ')
    ax.plot(x, y_real, color='green', label='Модель')
    ax.set(xlabel='X', ylabel='Y',
       title=title)
    ax.legend()
    ax.grid()
    fig.savefig(filename + fname + '.png', dpi=200)


def run_task_2():
    x = np.arange(-1.8, 2.1, 0.2)
    eps = np.random.normal(0, 1, size=20)
    # y = 2 + 2x + eps
    y = np.add(np.add(np.full(20, 2), x * 2), eps)
    # y2 with noise
    y2 = np.add(np.add(np.full(20, 2), x * 2), eps)
    y2[0] += 10
    y2[19] += -10

    if not os.path.exists(filename):
        os.mkdir(filename)

    lsm_0, lsm_1 = least_squares_coefs(x, y)
    lam_0, lam_1 = linear_approx_coefs(x, y)

    lsm_02, lsm_12 = least_squares_coefs(x, y2)
    lam_02, lam_12 = linear_approx_coefs(x, y2)

    with open(filename + "no_noise.tex", "w") as f:
        f.write("\\begin{enumerate}\n")
        f.write("\\item МНК, без возмущений:\n")
        f.write("$\hat{a}\\approx " + str(lsm_0) + "$, $\hat{b}\\approx " + str(lsm_1) + "$\n")
        f.write("\\item МНМ, без возмущений:\n")
        f.write("$\hat{a}\\approx " + str(lam_0) + "$, $\hat{b}\\approx " + str(lam_1) + "$\n")
        f.write("\\end{enumerate}\n")

    with open(filename + "noise.tex", "w") as f:
        f.write("\\begin{enumerate}\n")
        f.write("\\item МНК, с возмущенями:\n")
        f.write("$\hat{a}\\approx " + str(lsm_02) + "$, $\hat{b}\\approx " + str(lsm_12) + "$\n")
        f.write("\\item МНМ, с возмущенями:\n")
        f.write("$\hat{a}\\approx " + str(lam_02) + "$, $\hat{b}\\approx " + str(lam_12) + "$\n")
        f.write("\\end{enumerate}\n")

    draw(lsm_0, lsm_1, lam_0, lam_1, x, y, 'Выборка без возмущений', 'no_noise')
    draw(lsm_02, lsm_12, lam_02, lam_12, x, y2, 'Выборка с возмущенями', 'noise')

def main():
    run_task_2()

if __name__=='__main__':
    main()