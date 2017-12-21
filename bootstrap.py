
import numpy as np

from postgres import Postgres

pg = Postgres()

res = pg.query('SELECT x, y FROM linear_regression;')

print(res)

pg.close()
