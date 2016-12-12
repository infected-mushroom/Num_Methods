import math
import numpy as np
from tabulate import generate_uniform_grid, tabulate
from serializer import save_tabulated

def get_S(parameters):
    return lambda t: parameters['S(t)_a'] * t + np.sin(parameters['S(t)_b'] * t)


def get_z(parameters):
    return lambda t: parameters['z(t)_a'] * (t) + np.cos(parameters['z(t)_b'] * t)


def get_rho(parameters):
    return lambda w: parameters['p(w)_a'] * w * (parameters['p(w)_b']  - w)


def check_tabulation(rho_function, z_function, S_function, T):
    tabulated_rho = tabulate(rho_function, generate_uniform_grid(0, 1, 51))
    tabulated_z = tabulate(z_function, generate_uniform_grid(0, T, 51))
    tabulated_S = tabulate(S_function, generate_uniform_grid(0, T, 51))

    save_tabulated(tabulated_rho, 'files/tabulated_rho.txt')
    save_tabulated(tabulated_z, 'files/tabulated_z.txt')
    save_tabulated(tabulated_S, 'files/tabulated_S.txt')


def solve(**parameters):
    rho_function = get_rho(parameters)
    S_function = get_S(parameters)
    z_function = get_z(parameters)
    beta = parameters['Beta']
    T = parameters['T']
    x_0 = parameters['x_0']
    y_0 = parameters['y_0']
    check_tabulation(rho_function, z_function, S_function, T)

