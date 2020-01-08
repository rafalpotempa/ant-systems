import matplotlib.pyplot as plt

def plot(cities):
	for i, city in enumerate(cities):
		plt.scatter(city['x'], city['y'], c='skyblue')
		for anotherCity in cities[0:i] + cities[i+1:len(cities)]:
			plt.plot([city['x'], anotherCity['x']], [city['y'], anotherCity['y']], 'skyblue', linewidth=0.5)

	plt.show()