import numpy as np
from math import erf, gamma
from scipy.stats import poisson

# from numpy.random.mtrand import poisson

distributions = ['Normal', 'Cauchy', 'Laplace', 'Poisson', 'Uniform' ]
# distributions = ['Laplace']
loc, scale = 0.0, 1.0

def get_sample(name, size):
    if name == 'Normal':
        return np.random.normal(0, 1, size)
    elif name == 'Cauchy':
        return np.random.standard_cauchy(size)
    elif name == 'Laplace':
        return np.random.laplace(0, np.sqrt(2) / 2, size)
    elif name == 'Poisson':
        return np.random.poisson(10, size)
    elif name == 'Uniform':
        return np.random.uniform(-np.sqrt(3), np.sqrt(3), size)
    return []

def get_density_func(name, array):
    if name == 'Normal':
        return [1 / np.sqrt(2 * np.pi) * np.exp( - x ** 2 / (2 * 1 ** 2) ) for x in array]
    elif name == 'Cauchy':
        return [1 / (np.pi * (x ** 2 + 1) ) for x in array]
    elif name == 'Laplace':
        return [1 / np.sqrt(2) * np.exp(-np.sqrt(2) * np.fabs(x)) for x in array]
    elif name == 'Poisson':
        return [10 ** float(x) * np.exp(-10) / gamma(x + 1) for x in array]
    elif name == 'Uniform':
        return [1 / (2 * np.sqrt(3)) if abs(x) <= np.sqrt(3) else 0 for x in array]
    return []

def get_distr_func(name, x):
    if name == 'Normal':
        return 0.5 * (1 + erf(x / np.sqrt(2)))
    elif name == 'Cauchy':
        return np.arctan(x) / np.pi + 0.5
    elif name == 'Laplace':
        if x <= 0:
            return 0.5 * np.exp(np.sqrt(2) * x)
        else:
            return 1 - 0.5 * np.exp(-np.sqrt(2) * x)
    elif name == 'Poisson':
        return poisson.cdf(x, 10)
    elif name == 'Uniform':
        if x < -np.sqrt(3):
            return 0
        elif np.fabs(x) <= np.sqrt(3):
            return (x + np.sqrt(3)) / (2 * np.sqrt(3))
        else:
            return 1
    return 0
