from numpy import linspace

class TabulatedFunction:
    def __init__(self, grid, values):
        self.grid = grid
        self.values = values

    def __getitem__(self, key):
        return self.values[key]


def generate_uniform_grid(left, right, n):
    return linspace(left, right, num=n)


def tabulate(function, grid):
    return TabulatedFunction(grid=grid, values=[function(x) for x in grid])
