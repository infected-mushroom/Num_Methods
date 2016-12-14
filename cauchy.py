from tabulate import generate_uniform_grid

class Cauchy_Solution:

	def __init__(self, grid, solutions):
		self.grid = grid
		self.y = solutions

def solve_cauchy(f, x_0, y_0, left, right, n):
	y_prev = y_0
	y = [y_0]
	grid = generate_uniform_grid(left, right, n)
	for i in range(1, len(grid)):
	    y_i = y_prev + (grid[i] - grid[i - 1])*f(grid[i - 1], y_prev)
	    y.append(y_i)
	    y_prev = y_i
	return zip(grid, y)
#	return y
#	return Cauchy_Solution(grid, y)

'''f = lambda x, y: x**2 - 2*y
x_0 = 0
y_0 = 1
left = 0
right = 1
n = 11
#print solve_cauchy(f, x_0, y_0, left, right, n)'''
