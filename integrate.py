from tabulate import TabulatedFunction, generate_uniform_grid, tabulate

def integrate(function, left, right, n):
	grid = generate_uniform_grid(left, right, n)
	values = []
	first = 0.5*(grid[1] - grid[0])*(function(left))
	last = 0.5*(grid[1] - grid[0])*(function(right))
	sum = 0
	values.append(first)
	for i in range(1, len(grid) - 1):
		value = 0.5*(grid[i + 1] - grid[i - 1])*function(grid[i])
		sum += value
		values.append(sum)
	sum += last
	values.append(sum)
	return TabulatedFunction(grid=grid, values=values)
#	return zip(grid, values)


'''func = lambda x: x**2
left = 0
right = 5
n = 21
print integrate(func, left, right, n).values'''
