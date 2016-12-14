from tabulate import TabulatedFunction, generate_uniform_grid, tabulate

def integrate(function, left, right, n):
	grid = generate_uniform_grid(left, right, n)
#	values = [0.0]
	sum = 0.5*(grid[1] - grid[0])*(function(left) + function(right))

	for i in range(1, len(grid) - 1):
		value = 0.5*(grid[i + 1] - grid[i - 1])*function(grid[i])
		print value
		sum += value
	return sum


func = lambda x: x**2
left = 0
right = 5
n = 20
print integrate(func, left, right, n)

