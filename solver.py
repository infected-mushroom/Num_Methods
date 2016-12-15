from math import *
import numpy as np
from tabulate import generate_uniform_grid, tabulate
from integrate import integrate
from serializer import save_tabulated
from cauchy import solve_cauchy

def get_S(parameters):
     expression = "lambda t: " + str(parameters['S(t)'])
     return eval(expression)


def get_z(parameters):
     expression = "lambda t: " + str(parameters['z(t)'])
     return eval(expression)


def get_rho(parameters):
    expression = "lambda w: " + str(parameters['p(w)'])
    return eval(expression)


def check_tabulation(rho_function, z_function, S_function, T):
    tabulated_rho = tabulate(rho_function, generate_uniform_grid(0, T, 21))
    tabulated_z = tabulate(z_function, generate_uniform_grid(0, T, 21))
    tabulated_S = tabulate(S_function, generate_uniform_grid(0, T, 21))

    save_tabulated(tabulated_rho, 'files/tabulated_rho.txt')
    save_tabulated(tabulated_z, 'files/tabulated_z.txt')
    save_tabulated(tabulated_S, 'files/tabulated_S.txt')

def check_cauchy(function, x_0, y_0):
	solution = solve_cauchy(function, x_0, y_0, 0, 1, 11)
	np.savetxt('files/cauchy.txt', solution)

def check_integration(rho_function):
	integrated_rho = integrate(rho_function, 0, 1, 11)
	np.savetxt('files/rho_integrated.txt', integrated_rho)

def solve(**parameters):
    rho_function = get_rho(parameters)
    S_function = get_S(parameters)
    z_function = get_z(parameters)
    beta = parameters['Beta']
    T = parameters['T']
    x_0 = parameters['x_0']
    y_0 = parameters['y_0']
    check_tabulation(rho_function, z_function, S_function, T)
#    check_cauchy(z_function, x_0, y_0)
    check_integration(rho_function)
