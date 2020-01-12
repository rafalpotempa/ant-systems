from random import seed, randrange
from plot import *
from data.data import *
seed(0)

x, y = getData()
n = len(x)

cities = [{'n': i, 'x': x[i], 'y': y[i]} for i in range(n)]
T = [[0 for i in range(n)] for j in range(n)]
deltaT = [[1/n for i in range(n)] for j in range(n)]

ants = [{'init': randrange(0, n), 'path': []} for i in range(n)]

for ant in ants:
	pass

plot(cities)
