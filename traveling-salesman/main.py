from random import seed, randrange, uniform
from plot import *
from data import *
seed(0)

def distance(n1, n2):
	return ((cities[n1]['x'] - cities[n2]['x'])**2 + (cities[n1]['y'] - cities[n2]['y'])**2)**0.5

def sumTn(ant):
	sum = 0
	for city in cities:
		current = ant['path'][-1]
		if city['n'] in ant['path']:
			continue
		else:
			nj = 1/d[current][city['n']]
			sum += T[current][city['n']]**alpha * nj**beta
	return sum

alpha = 1
beta = 5
ro = 0.5
x, y = getData()
n = len(x)

cities = [{'n': i, 'x': x[i], 'y': y[i]} for i in range(n)]
T = [[1 for i in range(n)] for j in range(n)]
deltaT = [[1/n for i in range(n)] for j in range(n)]
d = [[distance(i, j) for i in range(n)] for j in range(n)]

ants = [{'init': randrange(0, n), 'path': [], 'dist': 0} for i in range(n*10)]
bestAnt = ants[0]

for k in range(50):
	for ant in ants:
		ant['path'] = [ant['init']]
		ant['dist'] = 0
		for i in range(n-1):
			a = []
			# find unattended cities
			for city in cities:
				current = ant['path'][-1]
				if city['n'] in ant['path']:
					continue
				else:
					Tj = T[current][city['n']]
					nj = 1/d[current][city['n']]
					aj = Tj**alpha * nj**beta / sumTn(ant)
					a.append({'n': city['n'], 'a': aj})
			p = []
			sumA = 0
			for aj in a:
				sumA += aj['a']

			# calculate probability
			for aj in a:
				p.append({'n': aj['n'], 'p': aj['a']/sumA})
			
			# make decision
			r = uniform(0, 1)
			sumP = 0
			for pj in p:
				sumP += pj['p']
				if r <= sumP:
					decision = pj['n']
					ant['path'].append(decision)
					break

		ant['path'].append(ant['init'])
		# count deltaT
		for i, city in enumerate(ant['path'][:-1]):
			n1 = ant['path'][i]
			n2 = ant['path'][i+1]

			dist = distance(n1, n2)
			ant['dist'] += dist

			deltaT[n1][n2] += 1/dist
			deltaT[n2][n1] += 1/dist

		if bestAnt['dist'] > ant['dist']:
			bestAnt = ant

	# update pheromone concentration
	for i, row in enumerate(T):
		for j, t in enumerate(row):
			T[i][j] = (1 - ro)*T[i][j] + deltaT[i][j]

print(bestAnt)
plot(cities, T, bestAnt)

