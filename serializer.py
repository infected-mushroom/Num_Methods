def save_tabulated(function, filename):
    with open(filename, 'w') as fout:
        print(serialize_tabulated(function), end='', file=fout)


def serialize_tabulated(function):
    result = ''
    for (argument, value) in zip(function.grid, function.values):
        result += '{} {}\n'.format(argument, value)
    return result
