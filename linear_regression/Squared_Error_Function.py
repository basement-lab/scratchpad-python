
import math
import numpy as np
import matplotlib.pyplot as plt

# ds = np.array([
#     # [0, 0],
#     [1, 1],
#     [2, 2],
#     [3, 3],
#     # [4, 4],
# ])

# ds = np.array([
#     [1, 2],
#     [2, 4],
#     [3, 6],
#     [4, 8],
#     [5, 10]])

ds = np.array([
    [1, 1.8],
    [2, 4.1],
    [3, 5.8],
    [4, 8.15],
    [5, 9.89]
])


def y_hat(i, slope):
    return slope * ds[i][0]


def cost_function_j(slope_guess):
    total = 0
    i = 0

    while i <= len(ds) - 1:
        y_i = ds[i][1]
        total = ((y_hat(i, slope_guess) - y_i) ** 2) + total
        i += 1

    return total * (1 / (2 * len(ds)))


print('(-3,', cost_function_j(-3), '),')
print('(-2,', cost_function_j(-2), '),')
print('(-1,', cost_function_j(-1), '),')
print('(0,', cost_function_j(0), '),')
print('(1,', cost_function_j(1), '),')
print('(2,', cost_function_j(2), '),')
print('(3,', cost_function_j(3), '),')
print('(4,', cost_function_j(4), '),')
print('(5,', cost_function_j(5), '),')
