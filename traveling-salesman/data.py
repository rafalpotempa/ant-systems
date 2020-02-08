import re
import sys

def getData():
	lines = []
	x, y = [], []
	with open('data/cities1.txt') as file:
		for line in file:
			lines.append(re.findall('\d+', line))

	x = [int(number) for number in lines[1]]
	y = [int(number) for number in lines[2]]
	return x, y
