import math
import numpy as np
import matplotlib.pyplot as plt

# ds = np.array([
#     [3, 5],
#     [2, 2],
#     [1, 9],
#     [6, 9]
# ])

ds = np.array([
    [1, 1.8],
    [2, 4.1],
    [3, 5.8],
    [4, 8.15],
    [5, 9.89]
])

def y_hat(i, slope):
    return slope * ds[i][0]


def cost_function(slope_guess):
    total = 0
    i = 0

    while i <= len(ds) - 1:
        y_i = ds[i][1]
        total = ((y_hat(i, slope_guess) - y_i) ** 2) + total
        i += 1

    return total * (1 / (2 * len(ds)))


def print_out():
    for i in range(0, len(ds)):
        print(i, cost_function(i))


print_out()
