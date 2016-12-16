from math import *
import numpy as np
from tabulate import generate_uniform_grid, tabulate
from integrate import integrate
from serializer import save_tabulated
from cauchy import solve_cauchy
from interpolation import Interpolation, interpolate
from differentiate import differentiate

import matplotlib.pyplot as plt
import matplotlib

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
	solution = solve_cauchy(function, x_0, y_0, 0, 1, 21)
	np.savetxt('files/cauchy.txt', solution)

def check_integration(rho_function):
	integrated_rho = integrate(rho_function, 0, 1, 21)
	np.savetxt('files/rho_integrated.txt', integrated_rho.values)

def check_interpolation(rho_function, z_function, S_function, T):
	tabulated_rho = tabulate(rho_function, generate_uniform_grid(0, T, 21))
	tabulated_z = tabulate(z_function, generate_uniform_grid(0, T, 21))
	tabulated_S = tabulate(S_function, generate_uniform_grid(0, T, 21))

	integrated_rho = integrate(rho_function, 0, 1, 21)

	interpolated_rho = interpolate(tabulated_rho).coefficients
	interpolated_z = interpolate(tabulated_z).coefficients
	interpolated_S = interpolate(tabulated_S).coefficients
	interpolated_U = interpolate(integrated_rho).coefficients
	np.savetxt('files/interpolated_rho.txt', interpolated_rho)
	np.savetxt('files/interpolated_S.txt', interpolated_S)
	np.savetxt('files/interpolated_z.txt', interpolated_z)
	np.savetxt('files/interpolated_U.txt', interpolated_U)


def solve(**parameters):
    rho_function = get_rho(parameters)
    S_function = get_S(parameters)
    z_function = get_z(parameters)
    beta = parameters['Beta']
    T = parameters['T']
    x_0 = parameters['x_0']
    y_0 = parameters['y_0']
    num_nodes = parameters['Num of grid nodes']
    check_tabulation(rho_function, z_function, S_function, T)
#    check_cauchy(z_function, x_0, y_0)
    check_integration(rho_function)
    check_interpolation(rho_function, z_function, S_function, T)
    integrated_rho = integrate(rho_function, 0, 1, 21)
    derivative = differentiate(z_function, 0, 1, 21)
    right_part = np.zeros(21)
    for i in range(21):
	right_part[i] = integrated_rho[i]*derivative[i]
    np.savetxt('files/right_part', right_part)
    x = solve_cauchy(right_part, x_0, y_0, 0, 1, 21)
    np.savetxt('files/x.txt', x)
    tabulated_S = tabulate(S_function, generate_uniform_grid(0, T, 21))
    S = np.asarray(tabulated_S.values)
    x = np.asarray(x)
    right_y = beta*(tabulated_S.values - x)
    np.savetxt('files/right_y.txt', right_y)
    y = solve_cauchy(right_y, x_0, y_0, 0, 1, 21)
    np.savetxt('files/y.txt', y)
    ns = np.arange(10, 3001, 10)

    errors1 = ns

    plt.rc('text', usetex=True)
    plt.xlabel('$\log n$')
    plt.ylabel('$\log E$')
    plt.plot(ns, errors1, label=r'$\sin(e^{2t})$')
    plt.legend(loc=1)
    plt.savefig('fig.png', bbox_inches='tight', figsize=(1, 1.6))

