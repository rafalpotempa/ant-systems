from random import seed, randrange
from plot import *
seed(0)

X = [0, 3, 6, 7, 15, 12, 14, 9, 7, 0]
Y = [1, 4, 5, 3, 0, 4, 10, 6, 9, 10]
n = len(X)

cities = [{'n': i, 'x': X[i], 'y': Y[i]} for i in range(n)]
T = [[0 for i in range(n)] for j in range(n)]
deltaT = [[1/n for i in range(n)] for j in range(n)]

ants = [{'init': randrange(0, n), 'path': []} for i in range(n)]

for ant in ants:
	pass

#plot(cities)
