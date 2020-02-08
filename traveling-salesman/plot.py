import matplotlib.pyplot as plt

def plot(cities, T, bestAnt):
	Tmax = 0
	for row in T:
		for t in row:
			if t > Tmax:
				Tmax = t

	for i, city in enumerate(cities):
		plt.scatter(city['x'], city['y'], c='royalblue')
		for anotherCity in cities[0:i] + cities[i+1:len(cities)]:
			lw = 0.5 + 3*T[city['n']][anotherCity['n']]/Tmax
			plt.plot([city['x'], anotherCity['x']], [city['y'], anotherCity['y']], c='gray', lw=lw, zorder=0)


	for i in range(len(cities)):
		n1 = bestAnt['path'][i]
		n2 = bestAnt['path'][i+1]
		plt.plot([cities[n1]['x'], cities[n2]['x']], [cities[n1]['y'], cities[n2]['y']], c='orange', zorder=0)
		
	for city in cities:
		plt.annotate(city['n'], (city['x'] + 0.1, city['y'] + 0.1))
	plt.show()