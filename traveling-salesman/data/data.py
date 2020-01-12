import re
import sys

def getData():
	lines = []
	with open('data/cities1.txt') as file:
		for line in file:
			lines.append(re.findall('\d+', line))
	x, y = lines[1], lines[2]
	return x, y
