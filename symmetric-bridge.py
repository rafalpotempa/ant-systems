from random import uniform

Rm, Lm = 0, 0

k, d = 20, 2

for i in range(200):
	Pr = (Rm + k)**d/((Rm + k)**d + (Lm + k)**d)
	
	r = uniform(0, 1)

	if r <= Pr:
		Rm += 1
	else:
		Lm += 1

print(Lm, Rm)
