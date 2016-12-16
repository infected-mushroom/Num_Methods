from tabulate import generate_uniform_grid

def differentiate(function, left, right, n):
	grid = generate_uniform_grid(left, right, n)
	derivative = [0.0]
	for i in range(len(grid) - 1):
		diff = float (function(grid[i + 1]) - function(grid[i])) / (grid[i + 1] - grid[i])
		derivative.append(diff)
	return derivative
