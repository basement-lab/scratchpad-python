
import numpy as np


def cost_func(ds, slope_guess):
    total = 0
    i = 0

    def y_hat(i, slope):
        return slope * ds[i][0]

    while i <= len(ds) - 1:
        y_i = ds[i][1]
        total = ((y_hat(i, slope_guess) - y_i) ** 2) + total
        i += 1

    return total * (1 / (2 * len(ds)))


__main__ = cost_func
