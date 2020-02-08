from random import seed, randrange, uniform
from plot import *
from data import *
seed(0)

def dist(n1, n2):
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
x, y = getData()
n = len(x)

cities = [{'n': i, 'x': x[i], 'y': y[i]} for i in range(n)]
T = [[1 for i in range(n)] for j in range(n)]
deltaT = [[1/n for i in range(n)] for j in range(n)]
d = [[dist(i, j) for i in range(n)] for j in range(n)]

ants = [{'init': randrange(0, n), 'path': []} for i in range(n)]

for ant in ants:
	# calculate probability
	ant['path'].append(ant['init'])
	for i in range(n-1):
		a = []
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

		for aj in a:
			p.append({'n': aj['n'], 'p': aj['a']/sumA})
		
		r = uniform(0, 1)
		sumP = 0
		for pj in p:
			sumP += pj['p']
			if r <= sumP:
				decision = p['n']


		break
	break


	# make decision

# plot(cities)

