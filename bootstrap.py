#!/usr/bin/env python

"""the world is your playground"""

from postgres import Postgres
from Squared_Error_Function import cost_func

PG = Postgres()

DATA = PG.query('SELECT x, y FROM linear_regression;')

PG.close()

print('-3', cost_func(DATA, -3))
print('-2', cost_func(DATA, -2))
print('-1', cost_func(DATA, -1))
print('0', cost_func(DATA, 0))
print('1', cost_func(DATA, 1))
print('2', cost_func(DATA, 2))
print('3', cost_func(DATA, 3))
print('4', cost_func(DATA, 4))
