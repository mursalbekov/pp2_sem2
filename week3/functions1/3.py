def ferm(numheads, numlegs):
	return numlegs/2 - numheads
numheads = 35
numlegs = 94
print("sum of rabbits = ", ferm(numheads, numlegs))
print("sum of chickens = ", numheads - ferm(numheads, numlegs))
