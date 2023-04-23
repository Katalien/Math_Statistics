import numpy as np

# Размеры выборок
sizes = [20, 60, 100]

# Значения коэффициента корреляции
rhos = [0, 0.5, 0.9]


def get_sample(size, rho):
    cov = [[1, rho], [rho, 1]]
    return np.random.multivariate_normal([0, 0], cov, size)