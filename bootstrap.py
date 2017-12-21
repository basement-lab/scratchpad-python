
import numpy as np

from postgres import Postgres
from Squared_Error_Function import cost_func

pg = Postgres()

ds = pg.query('SELECT x, y FROM linear_regression;')

pg.close()

print('-3', cost_func(ds, -3))
print('-2', cost_func(ds, -2))
print('-1', cost_func(ds, -1))
print('0', cost_func(ds, 0))
print('1', cost_func(ds, 1))
print('2', cost_func(ds, 2))
print('3', cost_func(ds, 3))
print('4', cost_func(ds, 4))

